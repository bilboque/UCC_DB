def get_players_order_rating_DESC(conn,curs):
    mysql_query="""SELECT * FROM JOUEURS ORDER BY RATING DESC"""
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat

def get_players_order_rating_AESC(conn,curs):
    mysql_query="""SELECT * FROM JOUEURS ORDER BY RATING"""
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat

def get_players_order_club_DESC(conn,curs):
    mysql_query="""SELECT * FROM JOUEURS ORDER BY CLUB DESC,RATING DESC"""
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat

def get_players_order_club_AESC(conn,curs):
    mysql_query="""SELECT * FROM JOUEURS ORDER BY CLUB,RATING DESC """
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat

def get_players_order_nom_DESC(conn,curs):
    mysql_query="""SELECT * FROM JOUEURS WHERE SURNAME<>'---' ORDER BY SURNAME DESC,RATING DESC """
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat

def get_players_order_nom_AESC(conn,curs):
    mysql_query="""SELECT * FROM JOUEURS WHERE SURNAME<>'---' ORDER BY SURNAME,RATING DESC """
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat

def get_players_with_Title(conn,curs):
    mysql_query="""SELECT * FROM JOUEURS WHERE TITLE<>'NONE' ORDER BY RATING DESC """
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat

def get_players_with_Games(conn,curs):
    mysql_query="""SELECT JoueurID, Name, Surname, Rating, Title, Club,(NB_W+NB_B) AS NB_PARTIES \
        FROM (SELECT COUNT(*) AS NB_W,WHITE FROM parties GROUP BY white ORDER BY COUNT(*) DESC) AS W,\
            (SELECT COUNT(*) AS NB_B,BLACK FROM parties GROUP BY BLACK ORDER BY COUNT(*) DESC) AS B, joueurs \
        WHERE W.white=B.BLACK AND W.white=JoueurID ORDER BY NB_PARTIES DESC"""
    curs.execute(mysql_query)
    joueurs = curs.fetchall()

    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]
        dico["rating"]=joueurs[3]
        dico["title"]=joueurs[4]
        dico["club"]=joueurs[5]

        resultat["data"].append(dico)

    return resultat


def get_player(conn,curs,id):
    mysql_query="""SELECT * FROM JOUEURS WHERE JoueurID=%s"""
    curs.execute(mysql_query,(id,))
    joueur = curs.fetchall()

    resultat = {}

    resultat["id"]=joueur[0][0]
    resultat["prenom"]=joueur[0][1]
    resultat["nom"]=joueur[0][2]
    resultat["rating"]=joueur[0][3]
    resultat["title"]=joueur[0][4]
    resultat["club"]=joueur[0][5]

    return resultat

def get_game_played_by_id(conn,curs,id):
    mysql_query="""SELECT PartieID,white.Name,black.name,winner.Name,Ouverture,format,sessions.Nom FROM joueurs as winner, joueurs as black, joueurs as white,parties,sessions \
        WHERE sessions.SessionID = parties.SessionID AND winner.JoueurID=Gagnant and black.JoueurID=black and white.JoueurID=white and (white=%s or black=%s)"""
    curs.execute(mysql_query,(id,id,))
    games = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for game in games:
        dico = {}
        dico["id"]=game[0]
        dico["blanc"]=game[1]
        dico["noir"]=game[2]
        dico["date"]=game[6]
        dico["gagnant"]=game[3]
        dico["ouverture"]=game[4]
        dico["format"]=game[5]

        resultat["data"].append(dico)

    return resultat

def get_player_winrate(conn,curs,id):
    mysql_query="""SELECT NB_WIN/(NB_W+NB_B) as WINRATE FROM \
        (SELECT COUNT(*) AS NB_W,WHITE FROM parties where white=%s GROUP BY white ORDER BY COUNT(*) DESC) AS W,\
        (SELECT COUNT(*) AS NB_B,BLACK FROM parties where black=%s GROUP BY BLACK ORDER BY COUNT(*) DESC) as B,\
        (SELECT COUNT(*) AS NB_WIN,gagnant FROM parties where gagnant=%s GROUP BY gagnant ORDER BY COUNT(*) DESC) as WIN;"""
    curs.execute(mysql_query,(id,id,id,))
    winrate = curs.fetchall()

    return winrate

def get_resultat_player(conn,curs,id):
    mysql_query="""Select Name,Surname,Nom,`Rank`,Points from\
          resultats,joueurs,sessions where resultats.JoueurID=joueurs.JoueurID and sessions.SessionID=resultats.SessionID and joueurs.JoueurID=%s order by Date DESC ,`Rank`;"""
    curs.execute(mysql_query,(id,))
    tournaments = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for tournament in tournaments:
        dico = {}
        dico["nom"]=tournament[0]
        dico["prenom"]=tournament[1]
        dico["tournoi"]=tournament[2]
        dico["resultat"]=tournament[3]
        dico["points"]=tournament[4]

        resultat["data"].append(dico)

    return resultat

def get_tournament_result(conn,curs,id):
    mysql_query="""Select Name,Surname,Nom,`Rank`,Points from\
          resultats,joueurs,sessions where resultats.JoueurID=joueurs.JoueurID and sessions.SessionID=resultats.SessionID and resultats.SessionID=%s  order by Date DESC ,`Rank`;"""
    curs.execute(mysql_query,(id,))
    tournaments = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for tournament in tournaments:
        dico = {}
        dico["nom"]=tournament[0]
        dico["prenom"]=tournament[1]
        dico["tournoi"]=tournament[2]
        dico["resultat"]=tournament[3]
        dico["points"]=tournament[4]

        resultat["data"].append(dico)

    return resultat

def get_tournament_infos(conn,curs):
    mysql_query="""SELECT SessionID,Nom,Date from sessions where Type='Tournoi' order by Date;"""
    curs.execute(mysql_query)
    tournaments = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for tournament in tournaments:
        dico = {}
        dico["id"]=tournament[0]
        dico["nom"]=tournament[1]
        dico["date"]=tournament[2]

        resultat["data"].append(dico)

    return resultat
