create table ouvertures
(
    nom_clef       varchar(255) not null
        primary key,
    nom_alternatif text         null,
    code_eco       varchar(255) null
);