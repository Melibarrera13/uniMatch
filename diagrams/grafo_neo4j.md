# Grafo Conceptual — UniMatch (Neo4j)

Representación del grafo de usuarios e intereses en Neo4j.

```mermaid
graph LR
    ANA["👤 Ana García\n(español)"]
    BRUNO["👤 Bruno López\n(español)"]
    CLARA["👤 Clara Méndez\n(español)"]
    DAVID["👤 David Torres\n(inglés)"]
    ELENA["👤 Elena Ruiz\n(español)"]

    UML["🏷️ UML"]
    BD["🏷️ Bases de Datos"]
    PY["🏷️ Python"]
    REDES["🏷️ Redes"]
    ALGO["🏷️ Algoritmos"]
    ML["🏷️ Machine Learning"]

    ANA -->|INTERES_EN| UML
    ANA -->|INTERES_EN| BD
    ANA -->|INTERES_EN| PY

    BRUNO -->|INTERES_EN| UML
    BRUNO -->|INTERES_EN| BD
    BRUNO -->|INTERES_EN| REDES

    CLARA -->|INTERES_EN| PY
    CLARA -->|INTERES_EN| ALGO
    CLARA -->|INTERES_EN| ML

    DAVID -->|INTERES_EN| PY
    DAVID -->|INTERES_EN| ML

    ELENA -->|INTERES_EN| UML
    ELENA -->|INTERES_EN| ALGO
```

## Matches que detecta el grafo

Cuando dos usuarios apuntan al mismo nodo `Interes`, Neo4j los detecta como posible match:

| Usuario 1 | Usuario 2 | Intereses en común |
|-----------|-----------|-------------------|
| Ana García | Bruno López | UML, Bases de Datos |
| Ana García | Clara Méndez | Python |
| Ana García | Elena Ruiz | UML |
| Clara Méndez | David Torres | Python, Machine Learning |
| Bruno López | Elena Ruiz | UML |

## Consulta Cypher equivalente

```cypher
MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
WHERE u1.nombre < u2.nombre
RETURN u1.nombre, u2.nombre, collect(i.nombre) AS intereses_comunes
```
