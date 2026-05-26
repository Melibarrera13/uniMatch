-- ===========================================
-- UniMatch - Schema PostgreSQL
-- Bases de Datos II
-- ===========================================

-- Limpiar tablas si ya existen
DROP TABLE IF EXISTS mensaje CASCADE;
DROP TABLE IF EXISTS match_academico CASCADE;
DROP TABLE IF EXISTS usuario_interes CASCADE;
DROP TABLE IF EXISTS interes CASCADE;
DROP TABLE IF EXISTS usuario CASCADE;

-- Tabla: usuario
CREATE TABLE usuario (
    id_usuario   SERIAL PRIMARY KEY,
    nombre       VARCHAR(100) NOT NULL,
    email        VARCHAR(150) UNIQUE NOT NULL,
    idioma       VARCHAR(50)  NOT NULL DEFAULT 'español'
);

-- Tabla: interes
CREATE TABLE interes (
    id_interes      SERIAL PRIMARY KEY,
    nombre_interes  VARCHAR(100) UNIQUE NOT NULL
);

-- Tabla: usuario_interes (relacion muchos a muchos)
CREATE TABLE usuario_interes (
    id_usuario  INT REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    id_interes  INT REFERENCES interes(id_interes) ON DELETE CASCADE,
    PRIMARY KEY (id_usuario, id_interes)
);

-- Tabla: match_academico
CREATE TABLE match_academico (
    id_match         SERIAL PRIMARY KEY,
    usuario1         INT REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    usuario2         INT REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    interes_en_comun VARCHAR(100)
);

-- Tabla: mensaje
CREATE TABLE mensaje (
    id_mensaje  SERIAL PRIMARY KEY,
    emisor      INT REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    receptor    INT REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    contenido   TEXT NOT NULL,
    fecha       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
