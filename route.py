from flask import Flask


# Começo da API:
app = Flask(__name__)

lista_de_compras = []

# Endpoint da raiz, index:
@app.route("/")
def index():
    return "Sua aplicação está funcionando!"

@app.route("/adicionar/")
def adicionar(item):
    lista_de_compras.append(item)
    return f'O item {item} foi adicionado a sua lista'

@app.route("/remover/")
def remover(item):
    lista_de_compras.remove(item)
    return f'O item "{item}" foi removido da sua lista' 

@app.route("/lista")
def lista():
    return lista_de_compras