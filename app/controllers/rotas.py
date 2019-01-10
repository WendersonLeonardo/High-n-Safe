from app import app
import csv,codecs
import pymysql
from  flask import render_template, request
from  datetime import  datetime
from pymysql import cursors
import pandas as pd
import folium
from folium import plugins

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
    conexao = pymysql.connect(host='localhost', user='root', password='root', db='mydb_ufrpe')

    c = conexao.cursor()
    consuta = '''select rpa_codigo,rpa_nome from sedecchamados;'''
    c.execute(consuta)
    resporta = c.fetchall()

    return (str(resporta))

@app.route("/m",methods=["GET", "POST"])
def mapacalor():
    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
    c = conexao.cursor()
    consulta = '''SELECT `Latitude`, `Longitude` FROM `Localidade do Chamado` WHERE `Endereco`!= "teste" or `Endereco`!= "TESTE";'''
    c.execute(consulta)
    resposta = c.fetchall()
    lista3=[]
    for x in resposta:
        try:
            lat = float(x[0])
            long = float(x[1])
            lista3.append([lat,long])

        except:
            print("error")
    pernambuco = folium.Map(location=[-8.0421584, -35.008676],zoom_start=10)

    #pernambuco.save('templates/hihihi.html')
    #iframe = pernambuco.repr_html_()
    pernambuco.add_child(plugins.HeatMap(lista3,min_opacity=0.7,max_val=0.5,))
    html_string = pernambuco.get_root().render()
    return (html_string)

@app.route("/mapaLonas")
def mapaLonas():
    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
    c = conexao.cursor()
    #consulta = ''' select Latitude,Longitude from `localidade do chamado` where idLocalidade in(SELECT `Localidade do Chamado_idLocalidade` FROM mydb_ufrpe.processo as p , mydb_ufrpe.vistoria as v where p.Numero = v.Processo_Numero); '''
    consulta = '''SELECT latitude,longitude FROM mydb_ufrpe.sedecchamados as c , mydb_ufrpe.sedeclonas as l where c.processo_numero = l.processo_numero and l.colocacao_lona_situacao = "Sim";'''
    c.execute(consulta)
    resposta = c.fetchall()
    lista3=[]
    for x in resposta:
        try:
            lat = float(x[0])
            long = float(x[1])
            lista3.append([lat,long])

        except:
            print("error")
    pernambuco = folium.Map(location=[-8.0421584, -35.008676],zoom_start=10)


    pernambuco.add_child(plugins.HeatMap(lista3,min_opacity=0.7,max_val=0.5,))
    html_string = pernambuco.get_root().render()
    return (html_string)




@app.route("/mapaCalorVistoria")
def mapaCalorVistoria():
    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
    c = conexao.cursor()
    #consulta = ''' select Latitude,Longitude from `localidade do chamado` where idLocalidade in(SELECT `Localidade do Chamado_idLocalidade` FROM mydb_ufrpe.processo as p , mydb_ufrpe.vistoria as v where p.Numero = v.Processo_Numero); '''
    consulta = '''SELECT `Latitude`, `Longitude` FROM `sedecvistorias` as vist, `sedecchamados` as chama WHERE vist.processo_numero = chama.processo_numero ;'''
    c.execute(consulta)
    resposta = c.fetchall()
    lista3=[]
    for x in resposta:
        try:
            lat = float(x[0])
            long = float(x[1])
            lista3.append([lat,long])

        except:
            print("error")
    pernambuco = folium.Map(location=[-8.0421584, -35.008676],zoom_start=10)


    pernambuco.add_child(plugins.HeatMap(lista3,min_opacity=0.7,max_val=0.5,))
    html_string = pernambuco.get_root().render()
    return (html_string)



@app.route("/mapaAcidentesVitimas")
def mapaAcidentesVitimas():
    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
    c = conexao.cursor()
    #consulta = ''' SELECT l.Latitude, l.Longitude FROM mydb_ufrpe.solicitacao as s , mydb_ufrpe.`localidade do chamado` as l where s.Houve_Vitimas = "Sim" and s.`Localidade do Chamado_idLocalidade`= l.idLocalidade; '''
    consulta = '''SELECT `latitude`,`longitude` FROM `sedecchamados` WHERE `solicitacao_vitimas` = "Sim" '''
    c.execute(consulta)
    resposta = c.fetchall()
    lista=[]
    for x in resposta:
        try:
            lat = float(x[0])
            long = float(x[1])
            lista.append([lat,long])

        except:
            print("error")

    pernambuco = folium.Map(location=[-8.0421584, -35.008676],zoom_start=10)
    #Marker
    for x in lista:
        folium.Marker(location =[x[0],x[1] ],
        popup='Acidente Com Vitima',
        icon=folium.Icon('red')
        ).add_to(pernambuco)

    html_string = pernambuco.get_root().render()
    return (html_string)


@app.route("/mapa")
def mapView():
    return render_template('mapaopcao.html')

@app.route("/mapaAcidentesVitimasFatais")
def mapaAcidentesVitimasFatais ():

    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
    c = conexao.cursor()

    #consulta= ''' SELECT l.Latitude, l.Longitude FROM mydb_ufrpe.solicitacao as s , mydb_ufrpe.`localidade do chamado` as l where s.Houve_Vitimas_fatais = "Sim" and s.`Localidade do Chamado_idLocalidade`= l.idLocalidade; '''
    consulta = '''SELECT `latitude`,`longitude` FROM `sedecchamados` WHERE `solicitacao_vitimas_fatais` = "Sim" '''
    c.execute(consulta)
    resposta = c.fetchall()
    lista=[]
    for x in resposta:
        try:
            lat = float(x[0])
            long = float(x[1])
            lista.append([lat,long])
        except:
            print("error")

    pernambuco = folium.Map(location=[-8.0421584, -35.008676],zoom_start=10)
    #Marker
    for x in lista:
        folium.Marker(location =[x[0],x[1] ],
        popup='Vitima Fatal - Morte',
        icon=folium.Icon('black')).add_to(pernambuco)

    html_string = pernambuco.get_root().render()
    return (html_string)

@app.route("/g")
def chartsView():
    return render_template('grafico.html')


@app.route("/r", methods=["GET", "POST"])
def totalInsidenteRpa():
    if request.method == "POST":

        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        conectar = conexao.cursor()

        regiao=request.form.get("comp_select_regiao")
        tipo_risco=request.form.get("comp_select_tipo_risco")
        ano=request.form.get("comp_select_ano")

        lista = []
        vitima = 0
        fatal = 0

        if regiao != '':
            comp_select_regiao = "and sc.rpa_codigo='%s'" %(regiao)
        if tipo_risco!='':
            comp_select_tipo_risco = "and sv.vistoria_risco='%s'" %(tipo_risco)
        if ano!='':
            comp_select_ano = "and sc.ano=%s " %(ano)

        isSelect="Select nome from rpa where id_rpa=%s" %(regiao)
        conectar.execute(isSelect)
        retorno = conectar.fetchall()
        lista.append(retorno)

        if tipo_risco!='' or regiao!= '' or ano!='':
            isSelect = """SELECT sc.solicitacao_vitimas, sc.solicitacao_vitimas_fatais FROM sedecchamados sc, sedecvistorias sv WHERE sc.processo_numero=sv.processo_numero %s %s %s""" %(comp_select_ano, comp_select_tipo_risco, comp_select_regiao)
            conectar.execute(isSelect)
            retorno = conectar.fetchall()

        else:
            isSelect = """select solicitacao_vitimas, solicitacao_vitimas_fatais from sedecchamados sc, sedecvistorias sv WHERE sc.processo_numero=sv.processo_numero """
            conectar.execute(isSelect)
            retorno = conectar.fetchall()

        for i in retorno:
            if i[0] == 'Sim':
                vitima += 1
            if i[1] == 'Sim':
                fatal += 1

        lista.append(vitima)
        lista.append(fatal)
        lista.append(len(retorno))
        return render_template('relatorio.html', lista=lista)
    else:
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
            if len(values) == 0:
                maximo = 0
            else:
                maximo = max(values)
            return render_template("grafico_tempo_medio.html", title='Grafico 1', max=maximo, labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
        else:
            return render_template("grafico_tempo_medio.html")
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

                c = conexao.cursor()
                consuta = '''
                select *
                from sedecchamados, sedecvistorias where sedecchamados.processo_numero = sedecvistorias.processo_numero and sedecchamados.rpa_codigo =''' + r + ''' and sedecchamados.ano =''' + comp_select_ano + ''' ;'''
                c.execute(consuta)
                resporta = c.fetchall()
                count_vis = len(resporta)

                if count_vis > count:
                    sub = count_vis - count
                else:
                    sub = count - count_vis
                values.append(sub)
            bar_labels = labels
            bar_values = values
            if len(values) == 0:
                maximo = 0
            else:
                maximo = max(values)
            return render_template("grafico_negligencia.html", title='Grafico 1', max=maximo, labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
        else:
            return render_template("grafico_negligencia.html")
    else:
        return render_template("grafico_negligencia.html")

@app.route("/grafico_risco", methods=["GET", "POST"])
def grafico_risco():
    if request.method == "POST":
        comp_select_ano = request.form.get("comp_select_ano")
        comp_select_risco = request.form.get("comp_select_risco")
        risco = '"'+ comp_select_risco +'"'
        conexao = pymysql.connect(host='localhost', user='root', password='root', db='mydb_ufrpe')
        values = []
        if  comp_select_ano != '' and comp_select_ano != None and comp_select_risco != '' and comp_select_risco != None :
            for r in rpa:
                c = conexao.cursor()
                consuta = '''SELECT COUNT(processo_numero) FROM sedecvistorias WHERE ano =''' + comp_select_ano + ''' AND vistoria_risco =''' + risco + ''' AND vistoria_rpa_codigo =''' + r + ''';'''
                c.execute(consuta)
                resporta = c.fetchall()
                valor = str(resporta)
                valor = valor.replace(')','')
                valor = valor.replace('(','')
                valor = valor.replace(',','')
                values.append(int(valor))
            bar_labels = labels
            bar_values = values
            if len(values)==0:
                maximo = 0
            else:
                maximo = max(values)
            return render_template("grafico_risco.html", title='Grafico 1', max=maximo, labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
        else:
            return render_template("grafico_risco.html")
    else:
        return render_template("grafico_risco.html")

@app.route("/grafico_incidente", methods=["GET", "POST"])
def grafico_incidente():
    if request.method == "POST":
        comp_select_ano = request.form.get("comp_select_ano")
        comp_select_incidente = request.form.get("comp_select_incidente")
        incidente = '"' + comp_select_incidente + '"'
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        values = []
        if comp_select_ano != '' and comp_select_ano != None and comp_select_incidente != '' and comp_select_incidente != None:
            for r in rpa:
                c = conexao.cursor()
                consuta = '''SELECT COUNT(sedecvistorias.processo_numero) FROM sedecvistorias, sedectipoocorrencias, sedecchamados WHERE sedecvistorias.processo_numero = sedectipoocorrencias.processo_numero AND sedecchamados.ano ='''+comp_select_ano+''' AND processo_ocorrencia ='''+incidente+''' AND sedecchamados.rpa_codigo ='''+r+''' AND sedecvistorias.processo_numero = sedecchamados.processo_numero;'''
                c.execute(consuta)
                resporta = c.fetchall()
                valor = str(resporta)
                valor = valor.replace(')','')
                valor = valor.replace('(','')
                valor = valor.replace(',','')
                values.append(int(valor))
            bar_labels = labels
            bar_values = values
            if len(values) == 0:
                maximo = 0
            else:
                maximo = max(values)
            return render_template("grafico_incidente.html", title='Grafico 1', max=maximo, labels=bar_labels,
                               values=bar_values, set=zip(values, labels, colors) )
        else:
            return render_template("grafico_incidente.html")
    else:
        return render_template("grafico_incidente.html")

@app.route("/grafico_vitima", methods=["GET", "POST"])
def grafico_vitima():
    if request.method == "POST":
        comp_select_ano = request.form.get("comp_select_ano")
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        values = []
        maximo = 0
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
    else:
        return render_template("grafico_vitima.html")
