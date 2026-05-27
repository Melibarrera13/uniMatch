# ===========================================
# UniMatch - CacheDAO (Redis)
# Bases de Datos II
# ===========================================

from redis_connection import get_redis


class CacheDAO:

    def __init__(self):
        self.r = get_redis()

    # --- Usuarios activos ---

    def marcar_usuario_activo(self, id_usuario, nombre, segundos=300):
        """Marca un usuario como activo con TTL."""
        self.r.setex(f"activo:usuario:{id_usuario}", segundos, nombre)

    def esta_activo(self, id_usuario):
        """Verifica si un usuario está activo en caché."""
        return self.r.get(f"activo:usuario:{id_usuario}")

    def obtener_activos(self, max_id=20):
        """Retorna lista de IDs y nombres de usuarios activos."""
        activos = []
        for i in range(1, max_id + 1):
            val = self.r.get(f"activo:usuario:{i}")
            if val:
                activos.append((i, val))
        return activos

    # --- Matches recientes ---

    def guardar_match_reciente(self, descripcion):
        """Agrega un match a la lista de recientes (máximo 10)."""
        self.r.lpush("matches_recientes", descripcion)
        self.r.ltrim("matches_recientes", 0, 9)  # mantener solo los últimos 10

    def obtener_matches_recientes(self):
        """Retorna los últimos matches guardados."""
        return self.r.lrange("matches_recientes", 0, -1)

    def limpiar_matches_recientes(self):
        self.r.delete("matches_recientes")

    # --- Intereses populares ---

    def registrar_interes(self, nombre_interes):
        """Suma 1 al contador de un interés."""
        self.r.zincrby("intereses_populares", 1, nombre_interes)

    def top_intereses(self, n=5):
        """Retorna los N intereses más populares."""
        return self.r.zrevrange("intereses_populares", 0, n - 1, withscores=True)


# --- Demo ---
if __name__ == "__main__":
    dao = CacheDAO()

    print("=== CacheDAO (Redis) ===\n")

    # Usuarios activos
    dao.marcar_usuario_activo(1, "Ana García")
    dao.marcar_usuario_activo(2, "Bruno López")
    dao.marcar_usuario_activo(3, "Clara Méndez")

    print("Usuarios activos:")
    for uid, nombre in dao.obtener_activos():
        print(f"  ID {uid}: {nombre}")

    print(f"\n¿Está activo el usuario 1? {dao.esta_activo(1)}")
    print(f"¿Está activo el usuario 99? {dao.esta_activo(99)}")

    # Matches recientes
    dao.limpiar_matches_recientes()
    dao.guardar_match_reciente("Ana García ↔ Bruno López (UML)")
    dao.guardar_match_reciente("Ana García ↔ Clara Méndez (Python)")
    dao.guardar_match_reciente("Clara Méndez ↔ David Torres (ML)")

    print("\nMatches recientes en caché:")
    for m in dao.obtener_matches_recientes():
        print(f"  {m}")

    # Intereses populares
    for i in ["UML", "UML", "UML", "Python", "Python", "Bases de Datos"]:
        dao.registrar_interes(i)

    print("\nTop intereses:")
    for nombre, score in dao.top_intereses():
        print(f"  {nombre}: {int(score)}")
