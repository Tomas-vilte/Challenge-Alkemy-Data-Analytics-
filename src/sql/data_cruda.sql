CREATE TABLE IF NOT EXISTS data_cruda (
    espacio_id        INTEGER PRIMARY KEY,
    Fecha_de_carga    TIMESTAMP,
    cod_localidad     INTEGER,
    id_provincia      INTEGER,
    id_departamento   INTEGER,
    categoria         VARCHAR(50),
    provincia         VARCHAR(50),
    localidad         VARCHAR(50),
    nombre            VARCHAR(50),
    domicilio         VARCHAR(50),
    codigo_postal     VARCHAR(10),
    numero            VARCHAR(20),
    mail              VARCHAR(50),
    web               VARCHAR(50)    
);