"""
Módulo de conexión a Redis.
Utiliza redis-py para conectarse al servidor de caché.
"""

import redis

# Parámetros de conexión
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# Instancia única del cliente Redis (singleton)
_redis_client = None

def get_redis_client():
    """
    Devuelve el cliente Redis. Si no existe, lo crea.
    decode_responses=True convierte bytes a strings automáticamente.
    """
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            decode_responses=True
        )
    return _redis_client

def init_redis():
    """
    Verifica la conexión a Redis al iniciar la aplicación.
    """
    client = get_redis_client()
    client.ping()  # Lanza excepción si no puede conectar
    print("[Redis] Conexión verificada con PING.")
