"""
Conexion a PostgreSQL para la demo Flask de UniMatch.
Usa el mismo contenedor y esquema del proyecto principal.
"""

import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "unimatch_db",
    "user": "admin",
    "password": "admin123",
}


def get_postgres_connection():
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)


def init_postgres():
    """Verifica que el schema del proyecto este cargado."""
    conn = get_postgres_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM usuario LIMIT 1")
        print("[PostgreSQL] Tabla 'usuario' disponible.")
    finally:
        cursor.close()
        conn.close()
