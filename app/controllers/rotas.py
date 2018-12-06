from app import app
import pymysql

from pymysql import cursors
@app.route("/")
def index():
    return ("Pagina Inicial, use /v para ver o banco")

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
    return ("Pagina do mapinha")