from flask import Flask,jsonify,render_template,request
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

@app.route("/organisateur",methods=['GET'])
def admin():
    return render_template("organisateur.html")


#api routes : /api/joueurs
#GET methods
@app.route("/api/joueurs/<order>",methods=['GET'])
def api_joueurs(order):
    result = get_players(connection,cursor,order)
    return jsonify(result)

@app.route("/api/joueurs/with_games",methods=['GET'])
def api_joueurs_with_games():
    result = get_players_with_Games(connection,cursor)
    return jsonify(result)

@app.route("/api/joueurs/with_titles",methods=['GET'])
def api_joueurs_with_title():
    result = get_players_with_Title(connection,cursor)
    return jsonify(result)

@app.route("/api/joueur/<id>",methods=['GET'])
def api_joueur_infos(id):
    result = get_player(connection,cursor,id)
    return jsonify(result)

@app.route("/api/joueurs_like/<like>",methods=['GET'])
def api_joueurs_like(like):
    result = get_players_like(connection,cursor,like)
    return jsonify(result)

@app.route("/api/gamesbyplayerid/<id>",methods=['GET'])
def api_games_by_player_id(id):
    result=get_game_played_by_id(connection,cursor,id)
    return jsonify(result)

@app.route("/api/winrate/<id>",methods=['GET'])
def api_get_winrate(id):
    result=get_player_winrate(connection,cursor,id)
    return jsonify(result)

@app.route("/api/resultats_tournois/<id>",methods=['GET'])
def api_get_resultats_joueurs(id):
    result=get_resultat_player(connection,cursor,id)
    return jsonify(result)

@app.route("/api/tournoi/<id>",methods=['GET'])
def api_get_resultats_tournois(id):
    result=get_tournament_result(connection,cursor,id)
    return jsonify(result)

@app.route("/api/tournois_infos",methods=['GET'])
def api_get_tournois_info():
    result=get_tournament_infos(connection,cursor)
    return jsonify(result)

@app.route("/api/ouvertures/",methods=['GET'])
def api_get_ouvertures():
    result=get_ouvertures(connection,cursor)
    return jsonify(result)

@app.route("/api/ouverture/<like>",methods=['GET'])
def api_get_ouverture(like):
    result=get_ouverture_like(connection,cursor,like)
    return jsonify(result)

@app.route("/api/ouverture_populaires/",methods=['GET'])
def api_get_ouverture_populaires():
    result=get_popular_openings(connection,cursor)
    return jsonify(result)

@app.route("/api/games_by_opening/<opening>",methods=['GET'])
def api_get_games_by_opening(opening):
    result=get_games_opening(connection,cursor,opening)
    return jsonify(result)

@app.route("/api/num_games_by_opening/<opening>",methods=['GET'])
def api_get_number_games_by_opening(opening):
    result=get_number_of_games_opening(connection,cursor,opening)
    return jsonify(result)

@app.route("/api/opening_joueur/<id>",methods=['GET'])
def api_get_openings_player(id):
    result=get_opening_joueur(connection,cursor,id)
    return jsonify(result)

@app.route("/api/opening_winrate/<opening>",methods=['GET'])
def api_get_opening_winrate(opening):
    result=get_opening_points_expectency(connection,cursor,opening)
    return jsonify(result)

#POST methods
@app.route('/api/new_player', methods=['POST'])
def new_player():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    titre = request.form.get('titre')
    club = request.form.get('club')
    rating = request.form.get('rating')

    query = "INSERT INTO joueurs (Surname, name, title, club, rating) VALUES (%s, %s, %s, %s, %s)"
    values = (nom, prenom, titre, club, rating)
    cursor.execute(query, values)
    connection.commit()

    return "Données du nouveau joueur insérées avec succès dans la base de données."