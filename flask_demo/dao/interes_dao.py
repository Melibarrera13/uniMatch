"""
DAO para intereses en Neo4j.
"""

from connections.neo4j_connection import get_neo4j_driver


def crear_interes(nombre):
    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run("MERGE (i:Interes {nombre: $nombre})", nombre=nombre)
    print(f"[InteresDAO] Interes '{nombre}' creado/verificado.")
    return nombre


def obtener_todos_intereses():
    driver = get_neo4j_driver()
    with driver.session() as session:
        resultado = session.run(
            "MATCH (i:Interes) RETURN i.nombre AS nombre ORDER BY i.nombre"
        )
        return [record["nombre"] for record in resultado]


def relacionar_usuario_interes(email_usuario, nombre_interes):
    driver = get_neo4j_driver()
    with driver.session() as session:
        resultado = session.run(
            """
            MATCH (u:Usuario {email: $email})
            MATCH (i:Interes {nombre: $interes})
            MERGE (u)-[:INTERES_EN]->(i)
            RETURN u.nombre AS usuario, i.nombre AS interes
            """,
            email=email_usuario,
            interes=nombre_interes,
        )
        record = resultado.single()
        if record:
            print(f"[InteresDAO] Relacion creada: {record['usuario']} -> {record['interes']}")
            return True
        print("[InteresDAO] No se encontro usuario o interes para relacionar.")
        return False


def buscar_usuarios_por_tema(tema):
    driver = get_neo4j_driver()
    with driver.session() as session:
        resultado = session.run(
            """
            MATCH (u:Usuario)-[:INTERES_EN]->(i:Interes {nombre: $tema})
            RETURN u.nombre AS nombre,
                   coalesce(u.email, '') AS email,
                   u.idioma AS idioma
            ORDER BY u.nombre
            """,
            tema=tema,
        )
        return [dict(record) for record in resultado]
