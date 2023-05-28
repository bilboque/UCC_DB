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

@app.route("/api/joueur/<id>")
def api_joueur_infos(id):
    result = get_player(connection,cursor,id)
    return jsonify(result)

@app.route("/api/gamesbyplayerid/<id>")
def api_games_by_player_id(id):
    result=get_game_played_by_id(connection,cursor,id)
    return jsonify(result)
