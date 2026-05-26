# DER — UniMatch (PostgreSQL)

Diagrama Entidad-Relación del modelo relacional de UniMatch.

```mermaid
erDiagram
    USUARIO {
        int id_usuario PK
        varchar nombre
        varchar email
        varchar idioma
    }

    INTERES {
        int id_interes PK
        varchar nombre_interes
    }

    USUARIO_INTERES {
        int id_usuario FK
        int id_interes FK
    }

    MATCH_ACADEMICO {
        int id_match PK
        int usuario1 FK
        int usuario2 FK
        varchar interes_en_comun
    }

    MENSAJE {
        int id_mensaje PK
        int emisor FK
        int receptor FK
        text contenido
        timestamp fecha
    }

    USUARIO ||--o{ USUARIO_INTERES : "tiene"
    INTERES ||--o{ USUARIO_INTERES : "asignado a"
    USUARIO ||--o{ MATCH_ACADEMICO : "participa (usuario1)"
    USUARIO ||--o{ MATCH_ACADEMICO : "participa (usuario2)"
    USUARIO ||--o{ MENSAJE : "envía"
    USUARIO ||--o{ MENSAJE : "recibe"
```

## Descripción de entidades

| Entidad | Descripción |
|---------|-------------|
| `usuario` | Persona registrada en UniMatch |
| `interes` | Tema o área académica de interés |
| `usuario_interes` | Relación muchos-a-muchos entre usuario e interés |
| `match_academico` | Pareja de usuarios con al menos un interés en común |
| `mensaje` | Mensaje enviado entre dos usuarios |
