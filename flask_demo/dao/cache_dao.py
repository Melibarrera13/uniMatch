"""
DAO para Caché con Redis.
Guarda las búsquedas realizadas y permite recuperar el historial.
"""

from connections.redis_connection import get_redis_client

# Clave de la lista de búsquedas recientes en Redis
CACHE_KEY_BUSQUEDAS = "busquedas_recientes"

# Máximo de búsquedas recientes a mantener
MAX_BUSQUEDAS = 10


def guardar_busqueda(tema):
    """
    Guarda una búsqueda en Redis usando una Lista.
    Estrategia:
      - LPUSH agrega el tema al inicio de la lista
      - LTRIM recorta la lista a los últimos MAX_BUSQUEDAS elementos
      - También se guarda con clave individual para contar repeticiones
    """
    client = get_redis_client()

    # Agregar al historial de búsquedas recientes
    client.lpush(CACHE_KEY_BUSQUEDAS, tema)
    client.ltrim(CACHE_KEY_BUSQUEDAS, 0, MAX_BUSQUEDAS - 1)

    # Incrementar contador de veces buscado (usando clave busqueda:<tema>)
    clave_contador = f"busqueda:{tema}"
    client.incr(clave_contador)
    # Expira en 1 hora (3600 segundos)
    client.expire(clave_contador, 3600)

    print(f"[CacheDAO] Búsqueda '{tema}' guardada en Redis.")


def obtener_busquedas_recientes():
    """
    Recupera las últimas búsquedas realizadas desde Redis.
    Devuelve lista de diccionarios con tema y cantidad de veces buscado.
    """
    client = get_redis_client()

    # Obtener la lista de búsquedas recientes
    temas = client.lrange(CACHE_KEY_BUSQUEDAS, 0, MAX_BUSQUEDAS - 1)

    resultado = []
    vistos = set()  # Para no repetir temas en el resumen

    for tema in temas:
        if tema not in vistos:
            vistos.add(tema)
            clave_contador = f"busqueda:{tema}"
            veces = client.get(clave_contador) or "1"
            resultado.append({
                "tema": tema,
                "veces": int(veces)
            })

    return resultado


def limpiar_cache():
    """
    Borra todo el historial de búsquedas de Redis.
    Útil para demostración en clase.
    """
    client = get_redis_client()
    client.delete(CACHE_KEY_BUSQUEDAS)
    print("[CacheDAO] Caché de búsquedas limpiado.")
