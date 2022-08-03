CREATE TABLE IF NOT EXISTS raw (
    Fecha_de_carga date PRIMARY KEY,
    cod_localidad     INTEGER NOT NULL,
    id_provincia      INTEGER NOT NULL,
    id_departamento   INTEGER NOT NULL,
    categoria         VARCHAR(50) NOT NULL,
    provincia         VARCHAR(50) NOT NULL,
    localidad         VARCHAR(50) NOT NULL,
    nombre            VARCHAR(50) NOT NULL,
    domicilio         VARCHAR(50) NOT NULL,
    codigo_postal     VARCHAR(10) NOT NULL,
    numero            VARCHAR(20) NOT NULL,
    mail              VARCHAR(50) NOT NULL,
    web               VARCHAR(50) NOT NULL    
);