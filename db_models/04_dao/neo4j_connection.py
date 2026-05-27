# ===========================================
# UniMatch - Conexión a Neo4j
# Bases de Datos II
# ===========================================

from neo4j import GraphDatabase

URI      = "bolt://localhost:7687"
USER     = "neo4j"
PASSWORD = "neo4j123"

def get_driver():
    """Retorna un driver de Neo4j."""
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    return driver


if __name__ == "__main__":
    try:
        driver = get_driver()
        driver.verify_connectivity()
        print("✅ Conexión a Neo4j exitosa")
        driver.close()
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
