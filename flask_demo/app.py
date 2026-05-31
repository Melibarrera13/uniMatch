"""
UniMatch - Aplicación Demo
===========================
Demo universitaria que integra PostgreSQL, Neo4j y Redis.

Rutas:
  GET  /               → Página principal
  GET  /usuarios        → Lista y formulario de usuarios
  POST /usuarios/crear  → Crea un usuario (PG + Neo4j)
  GET  /intereses       → Lista y formulario de intereses
  POST /intereses/crear → Crea un interés (Neo4j)
  POST /intereses/relacionar → Relaciona usuario con interés (Neo4j)
  GET  /buscar          → Busca usuarios por tema (Neo4j + Redis)
  GET  /matches         → Genera matches académicos (Neo4j)
  POST /cache/limpiar   → Limpia el historial de búsquedas (Redis)
"""

from flask import Flask, render_template, request, redirect, url_for, flash

# Importar inicializadores de conexiones
from connections.postgres_connection import init_postgres
from connections.neo4j_connection import init_neo4j, close_neo4j_driver
from connections.redis_connection import init_redis

# Importar DAOs
from dao.usuario_dao import crear_usuario, obtener_todos_usuarios
from dao.interes_dao import (
    crear_interes, obtener_todos_intereses,
    relacionar_usuario_interes, buscar_usuarios_por_tema
)
from dao.match_dao import generar_matches
from dao.cache_dao import guardar_busqueda, obtener_busquedas_recientes, limpiar_cache

# ─────────────────────────────────────────────
# Inicializar Flask
# ─────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = "unimatch_demo_2024"  # Necesario para flash messages


# ─────────────────────────────────────────────
# Inicializar bases de datos al arrancar
# ─────────────────────────────────────────────
def inicializar_bases():
    print("\n=== Inicializando conexiones ===")
    try:
        init_postgres()
    except Exception as e:
        print(f"[ERROR] PostgreSQL: {e}")

    try:
        init_neo4j()
    except Exception as e:
        print(f"[ERROR] Neo4j: {e}")

    try:
        init_redis()
    except Exception as e:
        print(f"[ERROR] Redis: {e}")

    print("=== Listo ===\n")


# ─────────────────────────────────────────────
# RUTAS
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Página principal con resumen del sistema."""
    return render_template("index.html")


# ── Usuarios ──────────────────────────────────

@app.route("/usuarios")
def usuarios():
    """Muestra la lista de usuarios y el formulario para crear uno nuevo."""
    lista = obtener_todos_usuarios()
    return render_template("usuarios.html", usuarios=lista)


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario_route():
    """
    Recibe los datos del formulario y crea el usuario en PostgreSQL y Neo4j.
    """
    nombre = request.form.get("nombre", "").strip()
    email  = request.form.get("email", "").strip()
    idioma = request.form.get("idioma", "").strip()

    if not nombre or not email or not idioma:
        flash("Todos los campos son obligatorios.", "error")
        return redirect(url_for("usuarios"))

    resultado = crear_usuario(nombre, email, idioma)
    if resultado:
        flash(f"Usuario '{nombre}' creado correctamente (ID PostgreSQL: {resultado}).", "success")
    else:
        flash(f"Error al crear usuario. El email '{email}' podría ya estar registrado.", "error")

    return redirect(url_for("usuarios"))


# ── Intereses ─────────────────────────────────

@app.route("/intereses")
def intereses():
    """Muestra intereses existentes y formularios para crear/relacionar."""
    lista_intereses = obtener_todos_intereses()
    lista_usuarios  = obtener_todos_usuarios()
    return render_template("intereses.html",
                           intereses=lista_intereses,
                           usuarios=lista_usuarios)


@app.route("/intereses/crear", methods=["POST"])
def crear_interes_route():
    """Crea un nodo (:Interes) en Neo4j."""
    nombre = request.form.get("nombre_interes", "").strip()
    if not nombre:
        flash("El nombre del interés no puede estar vacío.", "error")
        return redirect(url_for("intereses"))

    crear_interes(nombre)
    flash(f"Interés '{nombre}' creado en Neo4j.", "success")
    return redirect(url_for("intereses"))


@app.route("/intereses/relacionar", methods=["POST"])
def relacionar_route():
    """
    Crea la relación (Usuario)-[:INTERES_EN]->(Interes) en Neo4j.
    """
    email_usuario   = request.form.get("email_usuario", "").strip()
    nombre_interes  = request.form.get("nombre_interes_rel", "").strip()

    if not email_usuario or not nombre_interes:
        flash("Debes seleccionar un usuario y un interés.", "error")
        return redirect(url_for("intereses"))

    exito = relacionar_usuario_interes(email_usuario, nombre_interes)
    if exito:
        flash(f"Relación creada: {email_usuario} → {nombre_interes}", "success")
    else:
        flash("No se pudo crear la relación. Verificá que el usuario e interés existan.", "error")

    return redirect(url_for("intereses"))


# ── Búsqueda ──────────────────────────────────

@app.route("/buscar")
def buscar():
    """
    Busca usuarios por tema en Neo4j.
    Guarda la búsqueda en Redis y muestra el historial de búsquedas.
    """
    tema      = request.args.get("tema", "").strip()
    resultados = []
    busquedas_recientes = obtener_busquedas_recientes()

    if tema:
        # Buscar en Neo4j
        resultados = buscar_usuarios_por_tema(tema)
        # Guardar búsqueda en Redis (caché)
        guardar_busqueda(tema)
        # Refrescar historial después de guardar
        busquedas_recientes = obtener_busquedas_recientes()

    return render_template("buscar.html",
                           tema=tema,
                           resultados=resultados,
                           busquedas_recientes=busquedas_recientes)


# ── Matches ───────────────────────────────────

@app.route("/matches")
def matches():
    """
    Genera y muestra los matches académicos entre usuarios.
    Un match = dos usuarios con al menos un interés en común.
    """
    lista_matches = generar_matches()
    return render_template("matches.html", matches=lista_matches)


# ── Cache ─────────────────────────────────────

@app.route("/cache/limpiar", methods=["POST"])
def limpiar_cache_route():
    """Limpia el historial de búsquedas en Redis."""
    limpiar_cache()
    flash("Historial de búsquedas limpiado en Redis.", "success")
    return redirect(url_for("buscar"))


# ─────────────────────────────────────────────
# Punto de entrada
# ─────────────────────────────────────────────

if __name__ == "__main__":
    inicializar_bases()
    # debug=True recarga el servidor automáticamente al cambiar código
    app.run(debug=True, host="0.0.0.0", port=5000)
