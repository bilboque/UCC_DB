## UnigeChessClub database
![LOGO](CODE\static\UCC_Logo2.jpeg)

## Description
Developpement de l'interface web du ChessClub de l'Unige.
L'interface a pour but de facliter l'enregistrement des parties et des tournois joué lors des sessions.
Ce projet est a l'origine un projet pour le cour de Base de Données


## Installation
Ce projet utilise flask avec my-sql connector pour organiser les routes et la connection à la BD local.
Les tables (relations) de la BD peuvent être importé grace au différentes files .sql dans le dossier chessclub DB. Les données peuvent être importés depuis les .csv (lors de l'import fair attention a l'ID du Joueur DRAW, il doit être a 0, il faut donc le modifier manuellement depuis un SGBD si besoin après l'import).
Une fois l'instalation effectuer on peut lancer le site grace a la commande "python -m flask run" depuis un interpréteur python.

## Roadmap
Actuellent: implémentation de la gesion des tournois en swiss system directement depuis l'application.

Prochainement: ...

## Authors and acknowledgment
Developpeurs du projet: Julien Stalhandske, Andres Callealta et Léo Bonaz.

## License
...

## Project status
Work in progress...
