# ===========================================
# UniMatch - UsuarioDAO
# Bases de Datos II
# ===========================================

from postgres_connection import get_connection


class UsuarioDAO:

    def crear_usuario(self, nombre, email, idioma="español"):
        """Inserta un nuevo usuario en PostgreSQL."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO usuario (nombre, email, idioma) VALUES (%s, %s, %s) RETURNING id_usuario",
            (nombre, email, idioma)
        )
        id_nuevo = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return id_nuevo

    def obtener_todos(self):
        """Retorna todos los usuarios."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id_usuario, nombre, email, idioma FROM usuario ORDER BY id_usuario")
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas

    def obtener_por_id(self, id_usuario):
        """Retorna un usuario por su ID."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id_usuario, nombre, email, idioma FROM usuario WHERE id_usuario = %s", (id_usuario,))
        fila = cur.fetchone()
        cur.close()
        conn.close()
        return fila

    def eliminar_usuario(self, id_usuario):
        """Elimina un usuario por su ID."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
        conn.commit()
        cur.close()
        conn.close()


# --- Demo ---
if __name__ == "__main__":
    dao = UsuarioDAO()

    print("=== UsuarioDAO ===\n")

    print("Todos los usuarios:")
    for u in dao.obtener_todos():
        print(f"  {u}")

    print("\nUsuario con ID 1:")
    print(f"  {dao.obtener_por_id(1)}")
