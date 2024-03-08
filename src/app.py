from flask import Flask, render_template, request
from tinydb import TinyDB, Query
db = TinyDB('path/to/caminhos.json')
User = Query()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#cadastrar um novo conjunto de pontos em um caminho
@app.route("/novo", methods=["GET", "POST"])
def novo(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        db.insert(nome)
    return render_template("novo.html", nome=nome)

#recebe o id do caminho e devolve os pontos cadastrados nele
@app.route("pegar_caminho")
def pegar_caminho():
    return render_template("pegar_caminho.html")

#retorna o id e o nome de todos os caminhos cadastrados
@app.route("/listas_caminho")
def listas_caminho():
    dados = db.all()
    return render_template("listas_caminho.html", dados)


#atualiza o caminho cujo id foi fornecido
@app.route("/atualizar")
def atualizar():
    db.update()
    return render_template("atualizar.html")


#deleta o caminho com o id fornecido
@app.route("/deletar")
def deletar():
    db.remove()
    return render_template("deletar.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

