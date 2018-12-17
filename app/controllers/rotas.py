from app import app
import csv,codecs
#import pymysql
from  flask import render_template

#from pymysql import cursors
@app.route("/")
def index():
    #return ("Pagina Inicial, use /v para ver o banco")
    return render_template('index.html')

@app.route("/index")
def index2():
    #return ("Pagina Inicial, use /v para ver o banco")
    return render_template('index.html')

'''@app.route("/v")
def bdView():
    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')

    c = conexao.cursor()
    consuta = '''select rpa_codigo,rpa_nome from sedecchamados;'''
    c.execute(consuta)
    resporta = c.fetchall()

    for x in resporta:
        TrancaRua = int(x[0])
        Beuzebu = x[1]
        print("%s - %d" % (Beuzebu,TrancaRua))

'''
   # consulta = '''insert into rpa (id_rpa,nome) values (111,minhaJeba)''' 

    #c.execute(consulta)

    #return ("Cu")


@app.route("/m")
def mapacalor():
    return render_template('mapacalor.html')

@app.route("/m")
def mapView():
    return render_template('mapacalor.html')


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
