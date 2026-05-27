# ===========================================
# UniMatch - Conexión a Redis
# Bases de Datos II
# ===========================================

import redis

def get_redis():
    """Retorna un cliente de Redis."""
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r


if __name__ == "__main__":
    try:
        r = get_redis()
        r.ping()
        print("✅ Conexión a Redis exitosa")
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
