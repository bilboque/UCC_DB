create table sessions
(
    SessionID int auto_increment
        primary key,
    Date      date         null,
    Nom       varchar(255) null,
    Type      varchar(255) null
);

