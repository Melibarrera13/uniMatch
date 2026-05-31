"""
Módulo de conexión a Neo4j.
Utiliza el driver oficial neo4j para Python.
"""

from neo4j import GraphDatabase

# Parámetros de conexión
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "neo4j123"

# Instancia única del driver (singleton)
_driver = None

def get_neo4j_driver():
    """
    Devuelve el driver de Neo4j. Si no existe, lo crea.
    Patrón Singleton para reutilizar la conexión.
    """
    global _driver
    if _driver is None:
        _driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    return _driver

def close_neo4j_driver():
    """Cierra el driver al finalizar la aplicación."""
    global _driver
    if _driver:
        _driver.close()
        _driver = None
        print("[Neo4j] Driver cerrado.")

def init_neo4j():
    """
    Verifica la conexión a Neo4j al iniciar la aplicación.
    Crea índices básicos para mejorar el rendimiento.
    """
    driver = get_neo4j_driver()
    with driver.session() as session:
        # Índice sobre el email del Usuario para búsquedas rápidas
        session.run("""
            CREATE INDEX usuario_email IF NOT EXISTS
            FOR (u:Usuario) ON (u.email)
        """)
        # Índice sobre el nombre del Interes
        session.run("""
            CREATE INDEX interes_nombre IF NOT EXISTS
            FOR (i:Interes) ON (i.nombre)
        """)
    print("[Neo4j] Índices creados/verificados.")
