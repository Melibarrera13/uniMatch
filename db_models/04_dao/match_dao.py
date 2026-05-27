# ===========================================
# UniMatch - MatchDAO
# Bases de Datos II
# ===========================================

from postgres_connection import get_connection


class MatchDAO:

    def crear_match(self, usuario1, usuario2, interes_en_comun):
        """Inserta un match entre dos usuarios."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO match_academico (usuario1, usuario2, interes_en_comun) VALUES (%s, %s, %s) RETURNING id_match",
            (usuario1, usuario2, interes_en_comun)
        )
        id_nuevo = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return id_nuevo

    def obtener_todos(self):
        """Retorna todos los matches con nombres de usuario."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT m.id_match, u1.nombre, u2.nombre, m.interes_en_comun
            FROM match_academico m
            JOIN usuario u1 ON m.usuario1 = u1.id_usuario
            JOIN usuario u2 ON m.usuario2 = u2.id_usuario
            ORDER BY m.id_match
        """)
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas

    def obtener_matches_de_usuario(self, id_usuario):
        """Retorna todos los matches donde participa un usuario."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT m.id_match, u1.nombre, u2.nombre, m.interes_en_comun
            FROM match_academico m
            JOIN usuario u1 ON m.usuario1 = u1.id_usuario
            JOIN usuario u2 ON m.usuario2 = u2.id_usuario
            WHERE m.usuario1 = %s OR m.usuario2 = %s
        """, (id_usuario, id_usuario))
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas

    def calcular_posibles_matches(self):
        """Encuentra pares de usuarios con al menos un interés en común."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT u1.nombre, u2.nombre, i.nombre_interes
            FROM usuario_interes ui1
            JOIN usuario_interes ui2 ON ui1.id_interes = ui2.id_interes
                                    AND ui1.id_usuario < ui2.id_usuario
            JOIN usuario u1 ON ui1.id_usuario = u1.id_usuario
            JOIN usuario u2 ON ui2.id_usuario = u2.id_usuario
            JOIN interes i  ON ui1.id_interes  = i.id_interes
            ORDER BY u1.nombre, u2.nombre
        """)
        filas = cur.fetchall()
        cur.close()
        conn.close()
        return filas


# --- Demo ---
if __name__ == "__main__":
    dao = MatchDAO()

    print("=== MatchDAO ===\n")

    print("Matches registrados:")
    for m in dao.obtener_todos():
        print(f"  ID {m[0]}: {m[1]} ↔ {m[2]}  (interés: {m[3]})")

    print("\nMatches de la usuaria 1 (Ana):")
    for m in dao.obtener_matches_de_usuario(1):
        print(f"  {m[1]} ↔ {m[2]}  (interés: {m[3]})")

    print("\nPosibles matches por intereses en común:")
    for m in dao.calcular_posibles_matches():
        print(f"  {m[0]} ↔ {m[1]}  →  {m[2]}")
