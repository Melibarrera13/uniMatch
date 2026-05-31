"""
DAO para Matches académicos.
Genera coincidencias entre usuarios que comparten intereses
usando consultas de grafo en Neo4j.
"""

from connections.neo4j_connection import get_neo4j_driver


def generar_matches():
    """
    Encuentra pares de usuarios que comparten al menos un interés.

    Consulta Cypher:
      - Busca dos usuarios (u1, u2) que apunten al mismo nodo Interes
      - La condición u1.nombre < u2.nombre evita pares duplicados
        (Ana-Bruno y Bruno-Ana se reducen a un solo resultado)
      - collect(i.nombre) agrupa todos los intereses compartidos

    Retorna lista de diccionarios:
      [{ "usuario1": "Ana", "usuario2": "Bruno", "intereses": ["Python", "UML"] }]
    """
    driver = get_neo4j_driver()
    with driver.session() as session:
        resultado = session.run(
            """
            MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
            WHERE u1.nombre < u2.nombre
            RETURN u1.nombre AS usuario1,
                   u2.nombre AS usuario2,
                   collect(i.nombre) AS intereses_compartidos
            ORDER BY u1.nombre, u2.nombre
            """
        )
        matches = []
        for record in resultado:
            matches.append({
                "usuario1": record["usuario1"],
                "usuario2": record["usuario2"],
                "intereses": record["intereses_compartidos"]
            })
    print(f"[MatchDAO] Se encontraron {len(matches)} matches.")
    return matches
