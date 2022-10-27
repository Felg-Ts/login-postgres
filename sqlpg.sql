create table users(
    id serial primary key,
    username varchar(10) not null,
    password varchar(200) not null
);

INSERT INTO users (username, password) VALUES ('usuario', md5('usuario-2022'));

select md5('hola');

alter table users
alter column password
set data type varchar(200);