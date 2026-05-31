// ===========================================
// UniMatch - Grafo Neo4j
// Bases de Datos II
// ===========================================

// --- Limpiar la base antes de cargar ---
MATCH (n) DETACH DELETE n;

// --- Crear nodos de Usuario ---
CREATE (:Usuario {id: 1, email: 'ana@unimatch.com', nombre: 'Ana García',   idioma: 'español'});
CREATE (:Usuario {id: 2, email: 'bruno@unimatch.com', nombre: 'Bruno López',  idioma: 'español'});
CREATE (:Usuario {id: 3, email: 'clara@unimatch.com', nombre: 'Clara Méndez', idioma: 'español'});
CREATE (:Usuario {id: 4, email: 'david@unimatch.com', nombre: 'David Torres', idioma: 'inglés'});
CREATE (:Usuario {id: 5, email: 'elena@unimatch.com', nombre: 'Elena Ruiz',   idioma: 'español'});

// --- Crear nodos de Interes ---
CREATE (:Interes {nombre: 'UML'});
CREATE (:Interes {nombre: 'Bases de Datos'});
CREATE (:Interes {nombre: 'Python'});
CREATE (:Interes {nombre: 'Redes'});
CREATE (:Interes {nombre: 'Algoritmos'});
CREATE (:Interes {nombre: 'Machine Learning'});

// --- Relaciones Usuario → Interes ---
MATCH (u:Usuario {nombre: 'Ana García'}),   (i:Interes {nombre: 'UML'})             CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'Ana García'}),   (i:Interes {nombre: 'Bases de Datos'})  CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'Ana García'}),   (i:Interes {nombre: 'Python'})          CREATE (u)-[:INTERES_EN]->(i);

MATCH (u:Usuario {nombre: 'Bruno López'}),  (i:Interes {nombre: 'UML'})             CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'Bruno López'}),  (i:Interes {nombre: 'Bases de Datos'})  CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'Bruno López'}),  (i:Interes {nombre: 'Redes'})           CREATE (u)-[:INTERES_EN]->(i);

MATCH (u:Usuario {nombre: 'Clara Méndez'}), (i:Interes {nombre: 'Python'})          CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'Clara Méndez'}), (i:Interes {nombre: 'Algoritmos'})      CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'Clara Méndez'}), (i:Interes {nombre: 'Machine Learning'})CREATE (u)-[:INTERES_EN]->(i);

MATCH (u:Usuario {nombre: 'David Torres'}), (i:Interes {nombre: 'Python'})          CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'David Torres'}), (i:Interes {nombre: 'Machine Learning'})CREATE (u)-[:INTERES_EN]->(i);

MATCH (u:Usuario {nombre: 'Elena Ruiz'}),   (i:Interes {nombre: 'UML'})             CREATE (u)-[:INTERES_EN]->(i);
MATCH (u:Usuario {nombre: 'Elena Ruiz'}),   (i:Interes {nombre: 'Algoritmos'})      CREATE (u)-[:INTERES_EN]->(i);

// --- Relaciones de MATCH entre usuarios ---
MATCH (u1:Usuario {nombre: 'Ana García'}),  (u2:Usuario {nombre: 'Bruno López'})
CREATE (u1)-[:MATCH_CON {interes: 'UML, Bases de Datos'}]->(u2);

MATCH (u1:Usuario {nombre: 'Ana García'}),  (u2:Usuario {nombre: 'Clara Méndez'})
CREATE (u1)-[:MATCH_CON {interes: 'Python'}]->(u2);

MATCH (u1:Usuario {nombre: 'Clara Méndez'}),(u2:Usuario {nombre: 'David Torres'})
CREATE (u1)-[:MATCH_CON {interes: 'Python, Machine Learning'}]->(u2);


// ===========================================
// CONSULTAS ÚTILES PARA VERIFICAR
// ===========================================

// Ver todos los usuarios y sus intereses
// MATCH (u:Usuario)-[:INTERES_EN]->(i:Interes) RETURN u.nombre, i.nombre ORDER BY u.nombre;

// Buscar posibles matches: usuarios con intereses en común
// MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
// WHERE u1.nombre < u2.nombre
// RETURN u1.nombre, u2.nombre, collect(i.nombre) AS intereses_comunes;

// Ver matches ya registrados
// MATCH (u1:Usuario)-[m:MATCH_CON]->(u2:Usuario)
// RETURN u1.nombre, u2.nombre, m.interes;

// Recomendar por idioma + interés común
// MATCH (u1:Usuario)-[:INTERES_EN]->(i:Interes)<-[:INTERES_EN]-(u2:Usuario)
// WHERE u1.nombre < u2.nombre AND u1.idioma = u2.idioma
// RETURN u1.nombre, u2.nombre, i.nombre AS interes, u1.idioma AS idioma_comun;
