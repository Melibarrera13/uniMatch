# ===========================================
# UniMatch - MatchGraphDAO (Neo4j)
# Bases de Datos II
# ===========================================

from neo4j_connection import get_driver


class MatchGraphDAO:

    def __init__(self):
        self.driver = get_driver()

    def cerrar(self):
        self.driver.close()

    def agregar_usuario(self, id_usuario, nombre, idioma):
        """Crea un nodo Usuario en el grafo."""
        with self.driver.session() as session:
            session.run(
                "MERGE (u:Usuario {id: $id}) SET u.nombre = $nombre, u.idioma = $idioma",
                id=id_usuario, nombre=nombre, idioma=idioma
            )

    def agregar_interes(self, nombre_interes):
        """Crea un nodo Interes en el grafo."""
        with self.driver.session() as session:
            session.run(
                "MERGE (i:Interes {nombre: $nombre})",
                nombre=nombre_interes
            )

    def conectar_usuario_interes(self, nombre_usuario, nombre_interes):
        """Crea la relación (Usuario)-[:INTERES_EN]->(Interes)."""
        with self.driver.session() as session:
            session.run("""
                MATCH (u:Usuario {nombre: $usuario})
                MATCH (i:Interes {nombre: $interes})
                MERGE (u)-[:INTERES_EN]->(i)
            """, usuario=nombre_usuario, interes=nombre_interes)

    def recomendar_matches(self):
        """Retorna pares de usuarios con al menos un interés en común."""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
                WHERE u1.nombre < u2.nombre
                RETURN u1.nombre AS usuario1, u2.nombre AS usuario2,
                       collect(i.nombre) AS intereses_comunes
                ORDER BY size(collect(i.nombre)) DESC
            """)
            return [record.data() for record in result]

    def recomendar_por_idioma(self):
        """Retorna matches de usuarios con mismo idioma e interés en común."""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
                WHERE u1.nombre < u2.nombre AND u1.idioma = u2.idioma
                RETURN u1.nombre AS usuario1, u2.nombre AS usuario2,
                       i.nombre AS interes, u1.idioma AS idioma
                ORDER BY u1.nombre
            """)
            return [record.data() for record in result]

    def obtener_intereses_de_usuario(self, nombre_usuario):
        """Retorna los intereses de un usuario en el grafo."""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (u:Usuario {nombre: $nombre})-[:INTERES_EN]->(i:Interes)
                RETURN i.nombre AS interes
            """, nombre=nombre_usuario)
            return [r["interes"] for r in result]


# --- Demo ---
if __name__ == "__main__":
    dao = MatchGraphDAO()

    print("=== MatchGraphDAO (Neo4j) ===\n")

    print("Matches recomendados (por intereses en común):")
    for m in dao.recomendar_matches():
        print(f"  {m['usuario1']} ↔ {m['usuario2']}  →  {m['intereses_comunes']}")

    print("\nMatches con mismo idioma:")
    for m in dao.recomendar_por_idioma():
        print(f"  [{m['idioma']}] {m['usuario1']} ↔ {m['usuario2']}  →  {m['interes']}")

    print("\nIntereses de Ana García en el grafo:")
    print(f"  {dao.obtener_intereses_de_usuario('Ana García')}")

    dao.cerrar()
