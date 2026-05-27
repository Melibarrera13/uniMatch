# ===========================================
# UniMatch - MensajeDAO
# Bases de Datos II
# ===========================================

from postgres_connection import get_connection


class MensajeDAO:

    def enviar_mensaje(self, emisor, receptor, contenido):
        """Inserta un mensaje entre dos usuarios."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO mensaje (emisor, receptor, contenido) VALUES (%s, %s, %s) RETURNING id_mensaje",
            (emisor, receptor, contenido)
        )
        id_nuevo = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return id_nuevo

    def obtener_conversacion(self, usuario_a, usuario_b):
        """Retorna los mensajes entre dos usuarios, ordenados por fecha."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT u_e.nombre AS emisor, u_r.nombre AS receptor, m.contenido, m.fecha
            FROM mensaje m
            JOIN usuario u_e ON m.emisor   = u_e.id_usuario
            JOIN usuario u_r ON m.receptor = u_r.id_usuario
            WHERE (m.emisor = %s AND m.receptor = %s)
               OR (m.emisor = %s AND m.receptor = %s)
            ORDER BY m.fecha
        """, (usuario_a, usuario_b, usuario_b, usuario_a))
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas

    def obtener_todos(self):
        """Retorna todos los mensajes con nombres."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT u_e.nombre, u_r.nombre, m.contenido, m.fecha
            FROM mensaje m
            JOIN usuario u_e ON m.emisor   = u_e.id_usuario
            JOIN usuario u_r ON m.receptor = u_r.id_usuario
            ORDER BY m.fecha
        """)
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas


# --- Demo ---
if __name__ == "__main__":
    dao = MensajeDAO()

    print("=== MensajeDAO ===\n")

    print("Todos los mensajes:")
    for m in dao.obtener_todos():
        print(f"  [{m[3]}] {m[0]} → {m[1]}: {m[2]}")

    print("\nConversación entre Ana (1) y Bruno (2):")
    for m in dao.obtener_conversacion(1, 2):
        print(f"  {m[0]}: {m[2]}")
