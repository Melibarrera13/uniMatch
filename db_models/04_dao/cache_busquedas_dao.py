# ===========================================
# UniMatch - CacheBusquedasDAO
# Redis como caché de búsquedas recientes
# ===========================================

import redis


class CacheBusquedasDAO:

    def __init__(self):

        self.redis_client = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

    def guardar_busqueda(self, tema):

        self.redis_client.lpush(
            "busquedas_recientes",
            tema
        )

    def obtener_busquedas(self):

        return self.redis_client.lrange(
            "busquedas_recientes",
            0,
            9
        )


# ---------------- DEMO ----------------

if __name__ == "__main__":

    cache = CacheBusquedasDAO()

    print("\n=== Guardando búsquedas en Redis ===\n")

    cache.guardar_busqueda("Python")
    cache.guardar_busqueda("UML")
    cache.guardar_busqueda("Machine Learning")

    print("Búsquedas recientes:\n")

    for b in cache.obtener_busquedas():
        print(f"- {b}")
