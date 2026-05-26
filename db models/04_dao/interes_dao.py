# ===========================================
# UniMatch - InteresDAO
# Bases de Datos II
# ===========================================

from postgres_connection import get_connection


class InteresDAO:

    def crear_interes(self, nombre_interes):
        """Inserta un nuevo interés en PostgreSQL."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO interes (nombre_interes) VALUES (%s) RETURNING id_interes",
            (nombre_interes,)
        )
        id_nuevo = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return id_nuevo

    def obtener_todos(self):
        """Retorna todos los intereses."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id_interes, nombre_interes FROM interes ORDER BY id_interes")
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas

    def agregar_interes_a_usuario(self, id_usuario, id_interes):
        """Asocia un interés a un usuario."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO usuario_interes (id_usuario, id_interes) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            (id_usuario, id_interes)
        )
        conn.commit()
        cur.close()
        conn.close()

    def obtener_intereses_de_usuario(self, id_usuario):
        """Retorna los intereses de un usuario dado."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT i.id_interes, i.nombre_interes
            FROM interes i
            JOIN usuario_interes ui ON i.id_interes = ui.id_interes
            WHERE ui.id_usuario = %s
        """, (id_usuario,))
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas


# --- Demo ---
if __name__ == "__main__":
    dao = InteresDAO()

    print("=== InteresDAO ===\n")

    print("Todos los intereses:")
    for i in dao.obtener_todos():
        print(f"  {i}")

    print("\nIntereses del usuario 1 (Ana):")
    for i in dao.obtener_intereses_de_usuario(1):
        print(f"  {i}")
