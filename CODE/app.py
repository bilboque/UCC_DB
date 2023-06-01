from flask import Flask,jsonify,render_template
from mysql import connector

from request import *

#dsadasdsadas
connection = connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="chessclubdb"
)

cursor = connection.cursor()


app = Flask(__name__)
app.secret_key = "secret_key"


#main app pages

@app.route("/",methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/joueurs",methods=['GET'])
def joueurs():
    return render_template("joueurs.html")

@app.route("/joueur",methods=['GET'])
def joueur():
    return render_template("joueur.html")

@app.route("/tournois",methods=['GET'])
def tournois():
    return render_template("tournois.html")

@app.route("/ouvertures",methods=['GET'])
def ouvertures():
    return render_template("ouvertures.html")

@app.route("/ouverture",methods=['GET'])
def ouverture():
    return render_template("ouverture.html")


#api routes : /api/joueurs
@app.route("/api/joueurs/by_rating_DESC",methods=['GET'])
def api_joueurs_rating_desc():
    result = get_players_order_rating_DESC(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/by_rating_AESC",methods=['GET'])
def api_joueurs_order_rating_aesc():
    result = get_players_order_rating_AESC(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/by_club_DESC",methods=['GET'])
def api_joueurs_order_club_desc():
    result = get_players_order_club_DESC(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/by_club_AESC",methods=['GET'])
def api_joueurs_order_club_aesc():
    result = get_players_order_club_AESC(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/by_nom_DESC",methods=['GET'])
def api_joueurs_order_nom_desc():
    result = get_players_order_nom_DESC(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/by_nom_AESC",methods=['GET'])
def api_joueurs_order_nom_aesc():
    result = get_players_order_nom_AESC(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/with_games",methods=['GET'])
def api_joueurs_with_games():
    result = get_players_with_Games(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/with_titles",methods=['GET'])
def api_joueurs_with_title():
    result = get_players_with_Title(connection,cursor)
    return jsonify(result)

@app.route("/api/joueur/<id>")
def api_joueur_infos(id):
    result = get_player(connection,cursor,id)
    return jsonify(result)

@app.route("/api/gamesbyplayerid/<id>")
def api_games_by_player_id(id):
    result=get_game_played_by_id(connection,cursor,id)
    return jsonify(result)

@app.route("/api/winrate/<id>")
def api_get_winrate(id):
    result=get_player_winrate(connection,cursor,id)
    return jsonify(result)

@app.route("/api/resultats_tournois/<id>")
def api_get_resultats_joueurs(id):
    result=get_resultat_player(connection,cursor,id)
    return jsonify(result)

@app.route("/api/tournoi/<id>")
def api_get_resultats_tournois(id):
    result=get_tournament_result(connection,cursor,id)
    return jsonify(result)

@app.route("/api/tournois_infos")
def api_get_tournois_info():
    result=get_tournament_infos(connection,cursor)
    return jsonify(result)

@app.route("/api/ouvertures/")
def api_get_ouvertures():
    result=get_ouvertures(connection,cursor)
    return jsonify(result)

@app.route("/api/ouverture/<like>")
def api_get_ouverture(like):
    result=get_ouverture_like(connection,cursor,like)
    return jsonify(result)

@app.route("/api/ouverture_populaires/")
def api_get_ouverture_populaires():
    result=get_popular_openings(connection,cursor)
    return jsonify(result)

@app.route("/api/games_by_opening/<opening>")
def api_get_games_by_opening(opening):
    result=get_games_opening(connection,cursor,opening)
    return jsonify(result)

@app.route("/api/num_games_by_opening/<opening>")
def api_get_number_games_by_opening(opening):
    result=get_number_of_games_opening(connection,cursor,opening)
    return jsonify(result)

@app.route("/api/opening_joueur/<id>")
def api_get_openings_player(id):
    result=get_opening_joueur(connection,cursor,id)
    return jsonify(result)

@app.route("/api/opening_winrate/<opening>")
def api_get_opening_winrate(opening):
    result=get_opening_points_expectency(connection,cursor,opening)
    return jsonify(result)