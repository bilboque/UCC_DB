create table parties
(
    PartieID  int auto_increment
        primary key,
    white     int          null,
    black     int          null,
    gagnant   int          null,
    ouverture varchar(255) null,
    format    varchar(255) null,
    SessionID int          null
);

