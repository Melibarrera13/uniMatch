# ===========================================
# UniMatch - BuscarTemaDAO
# Lógica de negocio sobre Neo4j
# ===========================================

from neo4j_connection import get_driver


class BuscarTemaDAO:

    def __init__(self):
        self.driver = get_driver()

    def cerrar(self):
        self.driver.close()

    def buscar_usuarios_por_tema(self, tema):
        """
        Busca usuarios que tengan un interés específico.
        """

        with self.driver.session() as session:

            result = session.run("""
                MATCH (u:Usuario)-[:INTERES_EN]->(i:Interes)
                WHERE toLower(i.nombre) CONTAINS toLower($tema)

                RETURN
                    u.nombre AS usuario,
                    u.idioma AS idioma,
                    i.nombre AS interes

                ORDER BY u.nombre
            """, tema=tema)

            return [record.data() for record in result]


# ---------------- DEMO ----------------

if __name__ == "__main__":

    dao = BuscarTemaDAO()

    print("\n=== Buscar usuarios por tema ===\n")

    tema = "Python"

    resultados = dao.buscar_usuarios_por_tema(tema)

    if resultados:

        print(f"Usuarios encontrados para '{tema}':\n")

        for r in resultados:
            print(
                f"Usuario: {r['usuario']} | "
                f"Idioma: {r['idioma']} | "
                f"Interés: {r['interes']}"
            )

    else:
        print("No se encontraron usuarios.")

    dao.cerrar()
