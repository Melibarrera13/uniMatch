-- ===========================================
-- UniMatch - Datos de ejemplo
-- Bases de Datos II
-- ===========================================

-- Usuarios
INSERT INTO usuario (nombre, email, idioma) VALUES
    ('Ana García',    'ana@unimatch.com',    'español'),
    ('Bruno López',   'bruno@unimatch.com',  'español'),
    ('Clara Méndez',  'clara@unimatch.com',  'español'),
    ('David Torres',  'david@unimatch.com',  'inglés'),
    ('Elena Ruiz',    'elena@unimatch.com',  'español');

-- Intereses académicos
INSERT INTO interes (nombre_interes) VALUES
    ('UML'),
    ('Bases de Datos'),
    ('Python'),
    ('Redes'),
    ('Algoritmos'),
    ('Machine Learning');

-- Asignación de intereses a usuarios
-- Ana: UML, Bases de Datos, Python
INSERT INTO usuario_interes VALUES (1, 1), (1, 2), (1, 3);

-- Bruno: UML, Bases de Datos, Redes
INSERT INTO usuario_interes VALUES (2, 1), (2, 2), (2, 4);

-- Clara: Python, Algoritmos, Machine Learning
INSERT INTO usuario_interes VALUES (3, 3), (3, 5), (3, 6);

-- David: Python, Machine Learning
INSERT INTO usuario_interes VALUES (4, 3), (4, 6);

-- Elena: UML, Algoritmos
INSERT INTO usuario_interes VALUES (5, 1), (5, 5);

-- Matches generados por intereses en común
INSERT INTO match_academico (usuario1, usuario2, interes_en_comun) VALUES
    (1, 2, 'UML'),
    (1, 2, 'Bases de Datos'),
    (1, 3, 'Python'),
    (3, 4, 'Python'),
    (3, 4, 'Machine Learning');

-- Mensajes entre usuarios
INSERT INTO mensaje (emisor, receptor, contenido) VALUES
    (1, 2, '¡Hola Bruno! Vi que también te interesa UML.'),
    (2, 1, 'Sí, estoy estudiando para el parcial. ¿Hacemos grupo?'),
    (3, 4, 'David, ¿estás estudiando Machine Learning? Podríamos compartir recursos.');
