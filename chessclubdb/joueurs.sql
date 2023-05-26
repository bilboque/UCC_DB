create table joueurs
(
    JoueurID int auto_increment
        primary key,
    Name     varchar(255) null,
    Surname  varchar(255) null,
    Rating   int          null,
    Title    varchar(255) null,
    Club     varchar(255) null
);

