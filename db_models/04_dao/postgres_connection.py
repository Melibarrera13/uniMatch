# ===========================================
# UniMatch - Conexión a PostgreSQL
# Bases de Datos II
# ===========================================

import psycopg2

def get_connection():
    """Retorna una conexión activa a PostgreSQL."""
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="unimatch_db",
        user="admin",
        password="admin123"
    )
    return conn


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Conexión a PostgreSQL exitosa")
        conn.close()
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
