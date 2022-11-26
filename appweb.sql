create table users(
    id serial primary key,
    username varchar(10) not null,
    password varchar(200) not null
);

create table modulos(
    nombre varchar(80) primary key,
    horas_semanales integer,
    profesor varchar(15)
);

create table matriculaciones(
    alumnos integer REFERENCES users(id),
    modulos varchar(80) REFERENCES modulos(nombre),
    PRIMARY key (alumnos,modulos)

);

INSERT INTO users (username, password) VALUES ('usuario', md5('usuario-2022'));
INSERT INTO users (username, password) VALUES ('usuario1', md5('usuario1-2022'));
INSERT INTO users (username, password) VALUES ('usuario2', md5('usuario12-2022'));

INSERT INTO modulos (nombre, horas_semanales,profesor) VALUES ('Empresa e iniciativa emprendedora',4,'Maria Rosa');
INSERT INTO modulos (nombre, horas_semanales,profesor) VALUES ('Introducion a la computacion en la nube (HLC)',3,'Jose Domingo');
INSERT INTO modulos (nombre, horas_semanales,profesor) VALUES ('Implantacion de Aplicaciones Web',4,'Jose Domingo');
INSERT INTO modulos (nombre, horas_semanales,profesor) VALUES ('Servicios de Red e Internet',6,'Jose Domingo');
INSERT INTO modulos (nombre, horas_semanales,profesor) VALUES ('Seguridad y alta disponibilidad',4,'Raul');
INSERT INTO modulos (nombre, horas_semanales,profesor) VALUES ('Administracion de Sistemas Gestores de Bases de Datos',3,'Raul');
INSERT INTO modulos (nombre, horas_semanales,profesor) VALUES ('Administracion de Sistemas Operativos',6,'Rafael');

INSERT INTO matriculaciones (alumnos, modulos) VALUES (1,'Empresa e iniciativa emprendedora');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (1,'Introducion a la computacion en la nube (HLC)');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (1,'Implantacion de Aplicaciones Web');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (1,'Seguridad y alta disponibilidad');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (1,'Servicios de Red e Internet');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (1,'Administracion de Sistemas Gestores de Bases de Datos');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (1,'Administracion de Sistemas Operativos');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (2,'Introducion a la computacion en la nube (HLC)');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (2,'Implantacion de Aplicaciones Web');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (2,'Administracion de Sistemas Operativos');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (2,'Empresa e iniciativa emprendedora');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (3,'Introducion a la computacion en la nube (HLC)');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (3,'Implantacion de Aplicaciones Web');
INSERT INTO matriculaciones (alumnos, modulos) VALUES (3,'Servicios de Red e Internet');
