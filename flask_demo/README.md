# Demo web Flask - UniMatch

Esta carpeta contiene una demo web realizada con Flask e integrada al proyecto principal UniMatch.

La aplicacion usa los mismos servicios definidos en `docker-compose.yml`:

- PostgreSQL para usuarios y datos relacionales.
- Neo4j para intereses y relaciones de grafo.
- Redis para historial/cache de busquedas.

## Ejecutar

Desde la raiz del repositorio:

```bash
python -m pip install -r requirements.txt
python flask_demo/app.py
```

Abrir:

```text
http://localhost:5000
```

## Requisitos previos

Antes de abrir la demo, los contenedores deben estar levantados y los datos cargados:

```bash
docker compose up -d
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < "db_models/01_postgres/schema.sql"
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < "db_models/01_postgres/inserts.sql"
docker exec -i unimatch_neo4j cypher-shell -u neo4j -p neo4j123 < "db_models/02_neo4j/graph.cypher"
```
