from app import app
import csv,codecs
import pymysql
from  flask import render_template, request
from  datetime import  datetime
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
    conexao = pymysql.connect(host='www.db4free.net', user='alunoufrpe', password='ufrpe2018.2', db='mydb_ufrpe')

    c = conexao.cursor()
    consuta = '''select rpa_codigo,rpa_nome from sedecchamados;'''
    c.execute(consuta)
    resporta = c.fetchall()


    #consulta = '' #''''insert into rpa (id_rpa,nome) values (111,minhaJeba)'''

    #c.execute(consulta)

    return (str(resporta))


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


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
rpa = ['1', '2', '3', '4', '5', '6']
labels = ['RPA 1', 'RPA 2', 'RPA 3', 'RPA 4', 'RPA 5', 'RPA 6']

@app.route("/grafico_tempo_medio", methods=["GET", "POST"])
def grafico_tempo_medio():
    if request.method == "POST":
        comp_select_ano = request.form.get("comp_select_ano")
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        values = []
        if  comp_select_ano != '' and comp_select_ano != None:
            for r in rpa:
                c = conexao.cursor()
                consuta = '''select sedecvistorias.processo_numero, solicitacao_data, processo_data_conclusao 
                from sedecchamados, sedecvistorias 
                where sedecvistorias.processo_numero = sedecchamados.processo_numero 
                and sedecchamados.ano =''' + comp_select_ano + '''
                and rpa_codigo =''' + r +'''
                and processo_situacao = 'completo'
                and solicitacao_data IS NOT null
                and processo_data_conclusao IS NOT null;'''
                c.execute(consuta)
                resporta = c.fetchall()

                lista = []
                for x in resporta:
                    data_inicial = str(x[1])
                    data_final = str(x[2])
                    data_final = (data_final[0: 10].replace('/','-'))
                    #if data_final != '' and data_inicial != '':
                    date_init = datetime.strptime(data_inicial, "%Y-%m-%d").date()
                    date_final = datetime.strptime(data_final,"%Y-%m-%d").date()
                    subtracao = abs(date_final - date_init).days
                    lista.append(subtracao)

                if len(lista) > 0:
                    media = (sum(lista))/len(lista)
                    values.append(media)
                else:
                    values.append(0.0)
            bar_labels = labels
            bar_values = values
        return render_template("grafico_tempo_medio.html", title='Grafico 1', max=max(values), labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
    else:
        return render_template("grafico_tempo_medio.html")

@app.route("/grafico_negligencia", methods=["GET", "POST"])
def grafico_negligencia():
    if request.method == "POST":
        comp_select_ano = request.form.get("comp_select_ano")
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        values = []
        if  comp_select_ano != '' and comp_select_ano != None:
            for r in rpa:
                c = conexao.cursor()
                consuta = '''
                select *
                from sedecchamados where sedecchamados.rpa_codigo =''' + r + ''' and sedecchamados.ano =''' + comp_select_ano + ''' ;'''
                c.execute(consuta)
                resporta = c.fetchall()
                count = len(resporta)
                '''for i in resporta:
                    count+=1'''

                c = conexao.cursor()
                consuta = '''
                select *
                from sedecchamados, sedecvistorias where sedecchamados.processo_numero = sedecvistorias.processo_numero and sedecchamados.rpa_codigo =''' + r + ''' and sedecchamados.ano =''' + comp_select_ano + ''' ;'''
                c.execute(consuta)
                resporta = c.fetchall()

                count_vis = len(resporta)
                '''for i_vis in resporta:
                    count_vis+=1'''

                if count_vis > count:
                    sub = count_vis - count
                else:
                    sub = count - count_vis
                values.append(sub)
            bar_labels = labels
            bar_values = values
        return render_template("grafico_negligencia.html", title='Grafico 1', max=max(values), labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
    else:
        return render_template("grafico_negligencia.html")

@app.route("/grafico_risco", methods=["GET", "POST"])
def grafico_risco():
    if request.method == "POST":
        return render_template("grafico_risco.html", title='Grafico 1', max=max(values), labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
    else:
        return render_template("grafico_risco.html")

@app.route("/grafico_incidente", methods=["GET", "POST"])
def grafico_incidente():
    if request.method == "POST":
        return render_template("grafico_incidente.html", title='Grafico 1', max=max(values), labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
    else:
        return render_template("grafico_incidente.html")

@app.route("/grafico_vitima", methods=["GET", "POST"])
def grafico_vitima():
    if request.method == "POST":
        comp_select_ano = request.form.get("comp_select_ano")
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        values = []
        if  comp_select_ano != '' and comp_select_ano != None:
            for r in rpa:
                c = conexao.cursor()
                consuta = '''
                select distinct(sedecchamados.processo_numero) 
                            from Solicitacao, sedecchamados 
                            where sedecchamados.Processo_Numero = Solicitacao.processo_numero 
                            and Houve_Vitimas_fatais = 'Sim' 
                            and sedecchamados.rpa_codigo =''' + r + '''
                            and sedecchamados.ano =''' + comp_select_ano + ''' ;'''
                c.execute(consuta)
                resporta = c.fetchall()
                count = 0
                for i in resporta:
                    count+=1
                values.append(count)
            bar_labels = labels
            bar_values = values
        return render_template("grafico_vitima.html", title='Grafico 1', max=max(values), labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
    else:
        return render_template("grafico_vitima.html")