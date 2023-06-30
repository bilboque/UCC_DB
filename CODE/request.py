def get_players(conn,curs,order):
    mysql_query="SELECT * FROM JOUEURS where joueurid>0 ORDER BY " + order
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
    mysql_query="""SELECT * FROM JOUEURS WHERE TITLE<>'NONE' and joueurid>0 ORDER BY RATING DESC """
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
    mysql_query="""SELECT JoueurID, Name, Surname, Rating, Title, Club,count(*) from joueurs,parties where joueurid=white or joueurid=black group by joueurid order by count(*) DESC"""
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

def get_players_like(conn,curs,like):
    mysql_query="SELECT * FROM JOUEURS WHERE name like '%"+like+"%' LIMIT 5"
    curs.execute(mysql_query)
    joueurs = curs.fetchall()
    resultat = {}

    resultat["data"]=[]

    for joueurs in joueurs:
        dico = {}
        dico["id"]=joueurs[0]
        dico["prenom"]=joueurs[1]
        dico["nom"]=joueurs[2]

        resultat["data"].append(dico)

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
    mysql_query="""SELECT (NB_WIN + 0)/(NB_G + 0) as WINRATE FROM \
        (SELECT COUNT(*) AS NB_G,joueurid FROM joueurs,parties where (white=joueurid or black=joueurid) and %s=joueurid and (white=%s or black=%s) GROUP BY joueurid ORDER BY COUNT(*) DESC) AS W,\
        (SELECT COUNT(*) AS NB_WIN,gagnant FROM parties where gagnant=%s GROUP BY gagnant ORDER BY COUNT(*) DESC) as WIN;"""
    curs.execute(mysql_query,(id,id,id,id,))
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
    mysql_query="""Select Name,Surname,Nom,`Rank`,Points,Date from\
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
        dico["date"]=tournament[5]

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

def get_ouvertures(conn,curs):
    mysql_query="""SELECT * from ouvertures order by nom_clef;"""
    curs.execute(mysql_query)
    openings = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for opening in openings:
        dico = {}
        dico["nom"]=opening[0]
        dico["nom_alt"]=opening[1]
        dico["code"]=opening[2]

        resultat["data"].append(dico)

    return resultat

def get_ouverture_like(conn,curs,like):
    mysql_query="SELECT * from ouvertures where nom_alternatif like '%" + like +"%';" 
    curs.execute(mysql_query)
    openings = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for opening in openings:
        dico = {}
        dico["nom"]=opening[0]
        dico["nom_alt"]=opening[1]
        dico["code"]=opening[2]

        resultat["data"].append(dico)

    return resultat

def get_popular_openings(conn,curs):
    mysql_query="select nom_clef,code_eco,count(*) from ouvertures,parties where nom_clef=ouverture group by ouverture order by count(*) DESC;"
    curs.execute(mysql_query)
    openings = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for opening in openings:
        dico = {}
        dico["nom"]=opening[0]
        dico["code"]=opening[1]
        dico["nombre"]=opening[2]

        resultat["data"].append(dico)

    return resultat

def get_games_opening(conn,curs,opening):
    mysql_query="SELECT W.Name,B.Name,ouverture,Winner.Name from joueurs as W, joueurs as B,joueurs as Winner,ouvertures,parties where ouvertures.nom_alternatif like '%"+ opening +"%' and parties.ouverture = ouvertures.nom_clef and W.JoueurID=parties.white and B.JoueurID=parties.black and Winner.JoueurID=parties.gagnant;"
    curs.execute(mysql_query)
    openings = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for opening in openings:
        dico = {}
        dico["blanc"]=opening[0]
        dico["noir"]=opening[1]
        dico["ouverture"]=opening[2]
        dico["gagnant"]=opening[3]

        resultat["data"].append(dico)

    return resultat

def get_number_of_games_opening(conn,curs,opening):
    mysql_query="SELECT joueurid,name,count(*) from parties,joueurs,ouvertures where ouvertures.nom_alternatif like'%" + opening + "%' and (JoueurID=white or JoueurID=black) and  ouvertures.nom_clef = ouverture group by joueurid order by count(*) DESC"
    curs.execute(mysql_query)
    openings = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for opening in openings:
        dico = {}
        dico["id"]=opening[0]
        dico["name"]=opening[1]
        dico["count"]=opening[2]

        resultat["data"].append(dico)

    return resultat

def get_opening_joueur(conn,curs,id):
    mysql_query="select * from (select ouverture,count(*) as n_games from parties where (white = %s or black = %s) group by ouverture order by n_games DESC) as name where n_games >1"
    curs.execute(mysql_query,(id,id,))
    openings = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for opening in openings:
        dico = {}
        dico["ouverture"]=opening[0]
        dico["count"]=opening[1]

        resultat["data"].append(dico)

    return resultat

def get_opening_points_expectency(conn,curs,opening):
    mysql_query="select ((n_draw.n/2 + n_win.n)/n_games.n) from (select count(*) as n from parties, ouvertures where parties.ouverture = ouvertures.nom_clef and ouvertures.nom_alternatif like '%"+ opening +"%' and gagnant = white) as n_win, (select count(*) as n from parties, ouvertures where parties.ouverture = ouvertures.nom_clef and ouvertures.nom_alternatif like '%"+opening+"%' and gagnant = 0) as n_draw,(select count(*) as n from parties, ouvertures where parties.ouverture = ouvertures.nom_clef and ouvertures.nom_alternatif like '%"+opening+"%') as n_games"
    curs.execute(mysql_query)
    return curs.fetchall()

def get_sessions_like(conn,curs,nom_session):
    mysql_query="SELECT SessionID,Nom,Date from sessions where nom like '%" + nom_session + "%' order by Date DESC;"
    curs.execute(mysql_query)
    sessions = curs.fetchall()
    
    resultat = {}
    resultat["data"]=[]

    for session in sessions:
        dico = {}
        dico["id"]=session[0]
        dico["nom"]=session[1]

        resultat["data"].append(dico)

    return resultat