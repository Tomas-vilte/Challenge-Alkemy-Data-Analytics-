-- Procesar la información de cines para poder crear una tabla que contenga:
--  Provincia
--  Cantidad de pantallas
--  Cantidad de butacas
--  Cantidad de espacios INCAA
--  tabla con info de cines
CREATE TABLE IF NOT EXISTS cines (
    id                          INTEGER PRIMARY KEY,
    Fecha_de_carga              TIMESTAMP,
    Provincia                   VARCHAR(100),
    Pantallas                   INTEGER,
    Butacas                     INTEGER,
    espacio_INCAA               INTEGER
);