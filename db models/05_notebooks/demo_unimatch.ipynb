{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🎓 UniMatch — Demo del Proyecto\n",
    "**Bases de Datos II**\n",
    "\n",
    "Este notebook demuestra la integración entre **PostgreSQL**, **Neo4j** y **Redis** mediante la capa DAO del proyecto UniMatch.\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## ⚙️ Setup — agregar el path de los DAOs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import os\n",
    "\n",
    "# Agregar la carpeta dao al path para importar los módulos\n",
    "dao_path = os.path.abspath('../dao')\n",
    "if dao_path not in sys.path:\n",
    "    sys.path.insert(0, dao_path)\n",
    "\n",
    "print('✅ Path configurado:', dao_path)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## 1️⃣ PostgreSQL — Conexión y lectura de datos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from postgres_connection import get_connection\n",
    "\n",
    "try:\n",
    "    conn = get_connection()\n",
    "    print('✅ Conexión a PostgreSQL exitosa')\n",
    "    conn.close()\n",
    "except Exception as e:\n",
    "    print(f'❌ Error: {e}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ver todos los usuarios"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from usuario_dao import UsuarioDAO\n",
    "\n",
    "usuario_dao = UsuarioDAO()\n",
    "usuarios = usuario_dao.obtener_todos()\n",
    "\n",
    "print(f'Total de usuarios: {len(usuarios)}\\n')\n",
    "print(f'{\"ID\":<5} {\"Nombre\":<20} {\"Email\":<30} {\"Idioma\"}')\n",
    "print('-' * 65)\n",
    "for u in usuarios:\n",
    "    print(f'{u[0]:<5} {u[1]:<20} {u[2]:<30} {u[3]}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Crear un nuevo usuario"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nuevo_id = usuario_dao.crear_usuario('Fede Test', 'fede@test.com', 'español')\n",
    "print(f'✅ Usuario creado con ID: {nuevo_id}')\n",
    "\n",
    "# Verificar\n",
    "nuevo = usuario_dao.obtener_por_id(nuevo_id)\n",
    "print(f'Datos: {nuevo}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ver intereses de un usuario"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from interes_dao import InteresDAO\n",
    "\n",
    "interes_dao = InteresDAO()\n",
    "\n",
    "print('Todos los intereses disponibles:')\n",
    "for i in interes_dao.obtener_todos():\n",
    "    print(f'  {i[0]}. {i[1]}')\n",
    "\n",
    "print('\\nIntereses de Ana García (ID=1):')\n",
    "for i in interes_dao.obtener_intereses_de_usuario(1):\n",
    "    print(f'  → {i[1]}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Calcular posibles matches por intereses en común"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from match_dao import MatchDAO\n",
    "\n",
    "match_dao = MatchDAO()\n",
    "\n",
    "print('Posibles matches (pares con interés en común):')\n",
    "print(f'{\"Usuario 1\":<20} {\"Usuario 2\":<20} {\"Interés en común\"}')\n",
    "print('-' * 60)\n",
    "for m in match_dao.calcular_posibles_matches():\n",
    "    print(f'{m[0]:<20} {m[1]:<20} {m[2]}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ver matches registrados y mensajes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('Matches registrados en la base:')\n",
    "for m in match_dao.obtener_todos():\n",
    "    print(f'  Match #{m[0]}: {m[1]} ↔ {m[2]}  (interés: {m[3]})')\n",
    "\n",
    "print()\n",
    "\n",
    "from mensaje_dao import MensajeDAO\n",
    "mensaje_dao = MensajeDAO()\n",
    "\n",
    "print('Conversación entre Ana (1) y Bruno (2):')\n",
    "for m in mensaje_dao.obtener_conversacion(1, 2):\n",
    "    print(f'  {m[0]}: \"{m[2]}\"')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## 2️⃣ Neo4j — Grafo de relaciones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from neo4j_connection import get_driver\n",
    "\n",
    "try:\n",
    "    driver = get_driver()\n",
    "    driver.verify_connectivity()\n",
    "    print('✅ Conexión a Neo4j exitosa')\n",
    "    driver.close()\n",
    "except Exception as e:\n",
    "    print(f'❌ Error: {e}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Recomendaciones de match por el grafo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from match_graph_dao import MatchGraphDAO\n",
    "\n",
    "graph_dao = MatchGraphDAO()\n",
    "\n",
    "print('Matches recomendados por Neo4j (por intereses en común):')\n",
    "print(f'{\"Usuario 1\":<20} {\"Usuario 2\":<20} {\"Intereses en común\"}')\n",
    "print('-' * 65)\n",
    "for m in graph_dao.recomendar_matches():\n",
    "    intereses = ', '.join(m['intereses_comunes'])\n",
    "    print(f'{m[\"usuario1\"]:<20} {m[\"usuario2\"]:<20} {intereses}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Matches filtrados por idioma en común"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('Matches con mismo idioma (mayor compatibilidad):')\n",
    "for m in graph_dao.recomendar_por_idioma():\n",
    "    print(f'  [{m[\"idioma\"]}] {m[\"usuario1\"]} ↔ {m[\"usuario2\"]}  →  {m[\"interes\"]}')\n",
    "\n",
    "graph_dao.cerrar()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## 3️⃣ Redis — Caché de matches y usuarios activos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from redis_connection import get_redis\n",
    "\n",
    "try:\n",
    "    r = get_redis()\n",
    "    r.ping()\n",
    "    print('✅ Conexión a Redis exitosa')\n",
    "except Exception as e:\n",
    "    print(f'❌ Error: {e}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Simular usuarios activos y matches recientes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from cache_dao import CacheDAO\n",
    "\n",
    "cache = CacheDAO()\n",
    "\n",
    "# Marcar usuarios como activos\n",
    "cache.marcar_usuario_activo(1, 'Ana García')\n",
    "cache.marcar_usuario_activo(2, 'Bruno López')\n",
    "cache.marcar_usuario_activo(3, 'Clara Méndez')\n",
    "\n",
    "print('Usuarios activos ahora:')\n",
    "for uid, nombre in cache.obtener_activos():\n",
    "    print(f'  ✅ ID {uid}: {nombre}')\n",
    "\n",
    "print(f'\\n¿Está activo el usuario 4 (David)? {cache.esta_activo(4) or \"No\"}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Guardar matches recientes en caché\n",
    "cache.limpiar_matches_recientes()\n",
    "cache.guardar_match_reciente('Ana García ↔ Bruno López (UML)')\n",
    "cache.guardar_match_reciente('Ana García ↔ Clara Méndez (Python)')\n",
    "cache.guardar_match_reciente('Clara Méndez ↔ David Torres (Machine Learning)')\n",
    "\n",
    "print('Últimos matches en caché:')\n",
    "for m in cache.obtener_matches_recientes():\n",
    "    print(f'  📌 {m}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Top intereses\n",
    "for interes in ['UML', 'UML', 'UML', 'Python', 'Python', 'Bases de Datos', 'Machine Learning']:\n",
    "    cache.registrar_interes(interes)\n",
    "\n",
    "print('Top intereses más buscados:')\n",
    "for nombre, score in cache.top_intereses():\n",
    "    barra = '█' * int(score)\n",
    "    print(f'  {nombre:<20} {barra} ({int(score)})')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## ✅ Resumen\n",
    "\n",
    "| Base de Datos | Estado | Uso en UniMatch |\n",
    "|---------------|--------|----------------|\n",
    "| PostgreSQL    | ✅ OK  | Usuarios, intereses, matches, mensajes |\n",
    "| Neo4j         | ✅ OK  | Grafo de relaciones y recomendaciones |\n",
    "| Redis         | ✅ OK  | Caché de usuarios activos y matches recientes |\n",
    "\n",
    "**La capa DAO conecta los tres motores de forma simple y directa.** Cada DAO maneja su propia conexión y expone operaciones CRUD básicas."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
