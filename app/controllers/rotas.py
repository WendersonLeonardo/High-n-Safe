from app import app
import pymysql
from  flask import render_template

from pymysql import cursors
@app.route("/")
def index():
    #return ("Pagina Inicial, use /v para ver o banco")
    return render_template('index.html')

@app.route("/index")
def index2():
    #return ("Pagina Inicial, use /v para ver o banco")
    return render_template('index.html')

@app.route("/v")
def bdView():
    conexao = pymysql.connect(host='localhost',user='root',password='root',db='mydb')

    c = conexao.cursor()

    consulta = '''select * from mydb.sedecsolicitacoes where processo_numero in (SELECT processo_numero FROM mydb.sedecchamados where solicitacao_descricao = "teste") '''

    c.execute(consulta)

    resposta = c.fetchall()

    #print(resposta)

    return str(resposta)

@app.route("/m")
def mapView():
    # return ("Pagina do mapinha")
    return render_template('mapa.html')


@app.route("/g")
def chartsView():
    return render_template('grafico.html')


@app.route("/r")
def reportView():
    return render_template('relatorio.html')

@app.route("/contato")
def contatView():
    return render_template('contato.html')

@app.route("/sobre")
def aboutView():
    return render_template('sobre.html')
@app.route("/saiba_mais")

def moreView():
    return render_template('saiba_mais.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
