# 🎓 UniMatch — Plataforma de Matching Académico

> Proyecto universitario para la materia **Bases de Datos II**

UniMatch es una plataforma académica donde los usuarios se registran, crean un perfil, agregan intereses académicos, y el sistema recomienda otros usuarios con intereses similares.

**Ejemplo:**
- Usuario A agrega interés "UML"
- Usuario B agrega interés "UML"
- → el sistema los recomienda como posible match académico

---

## 🎯 Objetivo Académico

Demostrar la integración de múltiples motores de bases de datos mediante una capa DAO:

| Base de Datos | Rol en el proyecto |
|---------------|-------------------|
| **PostgreSQL** | Almacenamiento relacional principal |
| **Neo4j** | Grafo de relaciones entre usuarios e intereses |
| **Redis** | Caché de matches recientes y usuarios activos |

---

## 🗂 Estructura del repositorio

```
UniMatch/
├── README.md
├── requirements.txt
├── docker-compose.yml
│
├── db_models/
│   ├── 01_postgres/
│   │   ├── schema.sql          # Tablas y relaciones
│   │   └── inserts.sql         # Datos de ejemplo
│   │
│   ├── 02_neo4j/
│   │   └── graph.cypher        # Nodos y relaciones en grafo
│   │
│   ├── 03_redis/
│   │   └── redis_examples.py   # Ejemplos de uso del caché
│   │
│   ├── 04_dao/
│   │   ├── postgres_connection.py
│   │   ├── neo4j_connection.py
│   │   ├── redis_connection.py
│   │   ├── usuario_dao.py
│   │   ├── interes_dao.py
│   │   ├── match_dao.py
│   │   ├── mensaje_dao.py
│   │   ├── match_graph_dao.py
│   │   └── cache_dao.py
│   │
│   └── 05_notebooks/
│       └── demo_unimatch.ipynb  # Demo completa del proyecto
│
└── diagrams/
    ├── MER_postgres.md          # DER en Mermaid
    ├── grafo_neo4j.md           # Grafo conceptual
    └── arquitectura_general.md  # Arquitectura del sistema
```

---

## 🚀 Cómo levantar el proyecto con Docker

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/UniMatch.git
cd UniMatch
```

### 2. Levantar los contenedores

```bash
docker-compose up -d
```

Esto levanta:
- **PostgreSQL** en el puerto `5432`
- **Neo4j** en los puertos `7474` (browser) y `7687` (bolt)
- **Redis** en el puerto `6379`

### 3. Verificar que todo esté corriendo

```bash
docker-compose ps
```

### 4. Cargar el schema en PostgreSQL

```bash
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < db_models/01_postgres/schema.sql
docker exec -i unimatch_postgres psql -U admin -d unimatch_db < db_models/01_postgres/inserts.sql
```

### 5. Detener los contenedores

```bash
docker-compose down
```

---

## 🔌 Conectarse desde DBeaver

### PostgreSQL

| Campo | Valor |
|-------|-------|
| Host | `localhost` |
| Puerto | `5432` |
| Base de datos | `unimatch_db` |
| Usuario | `admin` |
| Contraseña | `admin123` |

### Neo4j Browser

Abrir en el navegador: http://localhost:7474

- Usuario: `neo4j`
- Contraseña: `neo4j123`

---

## 📓 Cómo ejecutar el Jupyter Notebook

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Lanzar Jupyter

```bash
jupyter notebook db_models/05_notebooks/demo_unimatch.ipynb
```

O desde el directorio raíz:

```bash
jupyter notebook
```

Luego navegar a `db_models/notebooks/demo_unimatch.ipynb`

---

## 🧪 Cómo probar la capa DAO

```bash
# Desde el directorio raíz del proyecto
cd db_models/04_dao

# Probar UsuarioDAO
python usuario_dao.py

# Probar MatchDAO
python match_dao.py

# Probar el grafo Neo4j
python match_graph_dao.py

# Probar caché Redis
python cache_dao.py
```

---

## 🔍 Ejemplos de consultas

### PostgreSQL — Usuarios con interés en común

```sql
SELECT u1.nombre, u2.nombre, i.nombre_interes
FROM usuario_interes ui1
JOIN usuario_interes ui2 ON ui1.id_interes = ui2.id_interes AND ui1.id_usuario < ui2.id_usuario
JOIN usuario u1 ON ui1.id_usuario = u1.id_usuario
JOIN usuario u2 ON ui2.id_usuario = u2.id_usuario
JOIN interes i ON ui1.id_interes = i.id_interes;
```

### Neo4j — Usuarios con intereses compartidos

```cypher
MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
WHERE u1.nombre <> u2.nombre
RETURN u1.nombre, u2.nombre, i.nombre AS interes_comun
```

### Redis — Ver matches cacheados

```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
print(r.lrange("matches_recientes", 0, -1))
```

---

## 📦 Tecnologías

- Python 3.10+
- PostgreSQL 15
- Neo4j 5
- Redis 7
- Docker & Docker Compose
- Jupyter Notebook
