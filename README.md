# UniMatch — Plataforma de Matching Académico

UniMatch es una plataforma académica donde los usuarios se registran, crean un perfil, agregan intereses académicos, y el sistema recomienda otros usuarios con intereses similares.

**Ejemplo:**
- Usuario A agrega interés "UML"
- Usuario B agrega interés "UML"
- → el sistema los recomienda como posible match académico

---

## Objetivo Académico

Demostrar la integración de múltiples motores de bases de datos mediante una capa DAO:

| Base de Datos | Rol en el proyecto |
|---------------|-------------------|
| **PostgreSQL** | Almacenamiento relacional principal |
| **Neo4j** | Grafo de relaciones entre usuarios e intereses |
| **Redis** | Caché de matches recientes y usuarios activos |

## Requisitos

Antes de ejecutar el proyecto se necesita:

- Git
- Docker Desktop en ejecución
- Python 3.10 o superior
- pip
- Opcional: DBeaver y Jupyter Notebook

## Estructura principal

```text
uniMatch/
├── docker-compose.yml
├── requirements.txt
├── db_models/
│   ├── 01_postgres/
│   │   ├── schema.sql
│   │   └── inserts.sql
│   ├── 02_neo4j/
│   │   └── graph.cypher
│   ├── 03_redis/
│   ├── 04_dao/
│   └── 05_notebooks/
│       └── demo_unimatch.ipynb
└── diagrams/
```


## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Melibarrera13/uniMatch.git
cd uniMatch
```

### 2. Levantar las bases de datos con Docker

```bash
docker compose up -d
```

Esto levanta:

- PostgreSQL: `localhost:5432`
- Neo4j Browser: `http://localhost:7474`
- Neo4j Bolt: `localhost:7687`
- Redis: `localhost:6379`

Para verificar:

```bash
docker compose ps
```

### 3. Cargar datos en PostgreSQL

En PowerShell:

```powershell
Get-Content "db_models\01_postgres\schema.sql" | docker exec -i unimatch_postgres psql -U admin -d unimatch_db
Get-Content "db_models\01_postgres\inserts.sql" | docker exec -i unimatch_postgres psql -U admin -d unimatch_db
```

En Git Bash, Linux o macOS:

```bash
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < "db_models/01_postgres/schema.sql"
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < "db_models/01_postgres/inserts.sql"
```

### 4. Cargar datos en Neo4j

En PowerShell:

```powershell
Get-Content "db_models\02_neo4j\graph.cypher" | docker exec -i unimatch_neo4j cypher-shell -u neo4j -p neo4j123
```

En Git Bash, Linux o macOS:

```bash
docker exec -i unimatch_neo4j cypher-shell -u neo4j -p neo4j123 < "db_models/02_neo4j/graph.cypher"
```

### 5. Instalar dependencias de Python

Se recomienda crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activarlo en Git Bash, Linux o macOS:

```bash
source .venv/Scripts/activate
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

### 6. Ejecutar el notebook

Usar:

```bash
python -m notebook "db_models/05_notebooks/demo_unimatch.ipynb"
```

Si aparece el error `No module named notebook`, instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

Luego volver a ejecutar el comando anterior.


## Demo web con Flask

El repositorio incluye una demo funcional en Flask dentro de `flask_demo/`. La demo permite navegar usuarios, intereses, búsquedas y matches usando PostgreSQL, Neo4j y Redis.

Antes de ejecutarla, levantar los contenedores y cargar los datos:

```bash
docker compose up -d
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < "db_models/01_postgres/schema.sql"
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < "db_models/01_postgres/inserts.sql"
docker exec -i unimatch_neo4j cypher-shell -u neo4j -p neo4j123 < "db_models/02_neo4j/graph.cypher"
```

Instalar dependencias y ejecutar Flask:

```bash
python -m pip install -r requirements.txt
python flask_demo/app.py
```

Abrir en el navegador:

```text
http://localhost:5000
```

## Datos de conexión

### PostgreSQL

| Campo | Valor |
| --- | --- |
| Host | `localhost` |
| Puerto | `5432` |
| Base de datos | `unimatch_db` |
| Usuario | `admin` |
| Contraseña | `admin123` |

### Neo4j

| Campo | Valor |
| --- | --- |
| Browser | `http://localhost:7474` |
| Bolt URI | `bolt://localhost:7687` |
| Usuario | `neo4j` |
| Contraseña | `neo4j123` |

### Redis

| Campo | Valor |
| --- | --- |
| Host | `localhost` |
| Puerto | `6379` |

## Probar conexiones desde Python

Desde la raíz del proyecto:

```bash
python "db_models/04_dao/postgres_connection.py"
python "db_models/04_dao/neo4j_connection.py"
python "db_models/04_dao/redis_connection.py"
```

## Apagar el proyecto

```bash
docker compose down
```

Si también se quieren borrar los volúmenes y datos cargados:

```bash
docker compose down -v
```

## Consultas de ejemplo

PostgreSQL:

```sql
SELECT u1.nombre, u2.nombre, i.nombre_interes
FROM usuario_interes ui1
JOIN usuario_interes ui2
  ON ui1.id_interes = ui2.id_interes
 AND ui1.id_usuario < ui2.id_usuario
JOIN usuario u1 ON ui1.id_usuario = u1.id_usuario
JOIN usuario u2 ON ui2.id_usuario = u2.id_usuario
JOIN interes i ON ui1.id_interes = i.id_interes;
```

Neo4j:

```cypher
MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
WHERE u1.nombre <> u2.nombre
RETURN u1.nombre, u2.nombre, i.nombre AS interes_comun;
```

Redis:

```python
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
print(r.keys("*"))
```
