-- Cantidad de registros totales por categoría
-- Tabla con registros totalizados por categoria
CREATE TABLE IF NOT EXISTS total_categoria (
    id                  INTEGER PRIMARY KEY,
    Fecha_de_carga      TIMESTAMP,
    categoria           VARCHAR(20),
    cantidad            INTEGER
);
