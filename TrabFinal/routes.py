from flask import Flask, jsonify
from  trab import lista as lista

app = Flask(__name__)

@app.route("/")
def listar_programacao():
    return jsonify ({'lista': lista()})

app.run(debug=True, port = 4999)