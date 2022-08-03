-- Cantidad de registros totales por fuente
-- Tabla con registros totalizados por fuente
CREATE TABLE IF NOT EXISTS total_fuente (
    id                  INTEGER PRIMARY KEY,
    Fecha_de_carga      TIMESTAMP,
    fuente              VARCHAR(100),
    cantidad            INTEGER
);