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


#api routes : /api/*
@app.route("/api/joueurs",methods=['GET'])
def api_joueurs_infos():
    result = get_players(connection,cursor)
    return jsonify(result)

@app.route("/api/joueur/<id>")
def api_joueur_infos(id):
    result = get_player(connection,cursor,id)
    return jsonify(result)
