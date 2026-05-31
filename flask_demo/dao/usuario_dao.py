"""
DAO de usuarios para la demo Flask.
Trabaja con PostgreSQL como fuente relacional y sincroniza nodos en Neo4j.
"""

from connections.postgres_connection import get_postgres_connection
from connections.neo4j_connection import get_neo4j_driver


def crear_usuario(nombre, email, idioma):
    """Crea un usuario en PostgreSQL y su nodo equivalente en Neo4j."""
    conn = get_postgres_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO usuario (nombre, email, idioma)
            VALUES (%s, %s, %s)
            RETURNING id_usuario
            """,
            (nombre, email, idioma),
        )
        usuario_id = cursor.fetchone()["id_usuario"]
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"[UsuarioDAO] Error PostgreSQL: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run(
            """
            MERGE (u:Usuario {email: $email})
            SET u.id = $id, u.nombre = $nombre, u.idioma = $idioma
            """,
            id=usuario_id,
            nombre=nombre,
            email=email,
            idioma=idioma,
        )

    print(f"[UsuarioDAO] Usuario '{nombre}' creado (id={usuario_id}).")
    return usuario_id


def obtener_todos_usuarios():
    """Devuelve usuarios de PostgreSQL con nombres de campos amigables para Flask."""
    conn = get_postgres_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT id_usuario AS id, nombre, email, idioma
            FROM usuario
            ORDER BY nombre
            """
        )
        usuarios = cursor.fetchall()
        return [dict(u) for u in usuarios]
    finally:
        cursor.close()
        conn.close()
