from neo4j_connection import get_driver

driver = get_driver()

try:
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n LIMIT 5")

        print("✅ Conexión exitosa a Neo4j\n")

        for record in result:
            print(record)

except Exception as e:
    print("❌ Error de conexión:")
    print(e)

finally:
    driver.close()
