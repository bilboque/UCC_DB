def get_players(conn,curs):
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
    mysql_query="""SELECT gameId,black.Name,white.name,date,winner.Name,Ouverture,format FROM joueurs as winner, joueurs as black, joueurs as white,parties WHERE winner.JoueurID=Gagnant and black.JoueurID=noir and white.JoueurID=blanc and (noir=%s or blanc=%s)"""
    curs.execute(mysql_query,(id,id,))
    games = curs.fetchall()

    resultat = {}
    resultat["data"]=[]

    for game in games:
        dico = {}
        dico["id"]=game[0]
        dico["blanc"]=game[1]
        dico["noir"]=game[2]
        dico["date"]=game[3]
        dico["gagnant"]=game[4]
        dico["ouverture"]=game[5]
        dico["format"]=game[6]

        resultat["data"].append(dico)

    return resultat
