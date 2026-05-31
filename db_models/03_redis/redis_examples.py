# ===========================================
# UniMatch - Ejemplos de uso de Redis
# Bases de Datos II
# ===========================================

import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

print("=== Ejemplos de Redis para UniMatch ===\n")

# --- 1. Guardar usuarios activos (SET con expiración) ---
print("1. Usuarios activos (expiran en 60 segundos):")
r.setex("activo:usuario:1", 60, "Ana García")
r.setex("activo:usuario:2", 60, "Bruno López")
r.setex("activo:usuario:3", 60, "Clara Méndez")

print("  Guardados: Ana, Bruno, Clara como activos")
print(f"  Usuario 1 activo: {r.get('activo:usuario:1')}")
print(f"  Usuario 99 activo: {r.get('activo:usuario:99')} (no existe)\n")

# --- 2. Caché de matches recientes (LISTA) ---
print("2. Matches recientes (lista):")
r.delete("matches_recientes")  # limpiar antes

r.lpush("matches_recientes", "Ana García - Bruno López (UML)")
r.lpush("matches_recientes", "Ana García - Clara Méndez (Python)")
r.lpush("matches_recientes", "Clara Méndez - David Torres (Machine Learning)")

matches = r.lrange("matches_recientes", 0, -1)
print("  Lista de matches recientes:")
for m in matches:
    print(f"    - {m}")
print()

# --- 3. Contador de intereses más buscados (SORTED SET) ---
print("3. Intereses más populares (sorted set):")
r.delete("intereses_populares")

r.zincrby("intereses_populares", 3, "UML")
r.zincrby("intereses_populares", 3, "Python")
r.zincrby("intereses_populares", 2, "Bases de Datos")
r.zincrby("intereses_populares", 2, "Machine Learning")
r.zincrby("intereses_populares", 1, "Redes")

top = r.zrevrange("intereses_populares", 0, -1, withscores=True)
print("  Ranking de intereses:")
for interes, score in top:
    print(f"    {interes}: {int(score)} usuarios")
print()

# --- 4. Hash de perfil rápido de usuario ---
print("4. Perfil rápido en caché (hash):")
r.delete("perfil:1")
r.hset("perfil:1", mapping={
    "nombre": "Ana García",
    "idioma": "español",
    "total_intereses": "3"
})

perfil = r.hgetall("perfil:1")
print(f"  Perfil cacheado de Ana: {perfil}\n")

# --- 5. Limpiar datos de prueba ---
print("5. Limpiando datos de prueba...")
r.delete("activo:usuario:1", "activo:usuario:2", "activo:usuario:3")
r.delete("matches_recientes", "intereses_populares", "perfil:1")
print("  Listo.\n")

print("=== Fin de los ejemplos de Redis ===")
