-- Cantidad de registros por provincia y categoría
-- Tabla con registros totalizados por provincia y categoría
CREATE TABLE IF NOT EXISTS prov_cat (
    id                  INTEGER PRIMARY KEY,
    Fecha_de_carga      TIMESTAMP,
    provincia           VARCHAR(100),
    categoria           VARCHAR(20),
    cantidad            INTEGER
);