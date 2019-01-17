from app import app
import csv,codecs
import pymysql
from  flask import render_template, request
from  datetime import  datetime
from pymysql import cursors
import pandas as pd
import folium
from folium import plugins
from branca.element import *

@app.route('/opcaorpa', methods = ["GET", "POST"])
def opcaorpa():

    if request.method == "GET":
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        c = conexao.cursor()

        #estatisticas
        
        consulta2 = '''SELECT `nome` ,count(`rpa_id_rpa`)
        from `Localidade do Chamado` as l ,`rpa` as r
        WHERE r.`id_rpa` = l.`rpa_id_rpa` GROUP BY `rpa_id_rpa` '''
        
        
        c.execute(consulta2)
        re = c.fetchall()
        re2 =[]
        total = 0
        for x in re:
            total = x[1] + total



        for x in re:
            nomeRpa = x[0]
            qtdChamados = x[1]
            link = 'http://www2.recife.pe.gov.br/servico/sobre-rpa-' + nomeRpa[0]
            percentual = qtdChamados/total*100
            string = ("%.2f" % percentual)
            re2.append([nomeRpa, qtdChamados, link, string])


        re2.sort(reverse = True,key=lambda x:x[1])
        return render_template('mapacalorporrpa.html',rpa = re2)

    if request.method == "POST":
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        c = conexao.cursor()

        rpa1 = '1-CENTRO'
        rpa2 = '2-NORTE'
        rpa3 = '3-NOROESTE'
        rpa4 = '4-NORDESTE'
        rpa5 = '5-SUDOESTE'
        rpa6 = '6-SUL'


        retorno = request.form.get("rpa_opcao")
        

        def Calango(verde):

            a = verde
            if a == False:
                consulta = '''SELECT `Latitude`, `Longitude`,rpa_id_rpa FROM
                `Localidade do Chamado`
                WHERE (`Endereco`!= "teste" or `Endereco`!= "TESTE") ;'''
            else:

                consulta = '''SELECT `Latitude`, `Longitude`,rpa_id_rpa FROM
                `Localidade do Chamado`
                WHERE (`Endereco`!= "teste" or `Endereco`!= "TESTE") and `rpa_id_rpa` = '''+a+''';'''

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
            map_path = app.root_path + '/templates' + '/' + 'map_test2.html'
            pernambuco.save(map_path)

            
        
        
        if retorno == "RPA1":
            Calango('1')
            return render_template("mapacalor.html")
            

        if retorno == 'RPA2':
            Calango('2')
            return render_template("mapacalor.html")
            

        if retorno == "RPA3":
           Calango('3')
           return render_template("mapacalor.html")
            


        if retorno == 'RPA4':
            Calango('4')
            return render_template("mapacalor.html")
            
        
        if retorno == "RPA5":
            Calango('5')
            return render_template("mapacalor.html")
            

        if retorno == "RPA6":
            Calango('6')
            return render_template("mapacalor.html")
            

        if retorno == "Todas":
            Calango(False)
            return render_template("mapacalor.html")
            

    #return render_template('mapacalorporrpa.html')
    


@app.route("/m",methods=["GET", "POST"])
def mapacalor():

   

    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
    c = conexao.cursor()




@app.route("/mapaLonas",methods=["GET", "POST"])
def mapaLonas():
    if request.method == "POST":
        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        c = conexao.cursor()
        
        def Calango(verde):

            a = verde

            if a == False:
                
                consulta = '''SELECT latitude,longitude 
                FROM mydb_ufrpe.processo as p , mydb_ufrpe.`Colocacao Lonas` as c, mydb_ufrpe.`Localidade do Chamado` as l 
                where p.Numero = c.Processo_Numero and c.situacao = 'Sim' and p.`Localidade do Chamado_idLocalidade` = l.idLocalidade
                '''

            else:
                
                
                consulta = '''SELECT latitude,longitude 
                FROM mydb_ufrpe.processo as p , mydb_ufrpe.`Colocacao Lonas` as c, mydb_ufrpe.`Localidade do Chamado` as l 
                where p.Numero = c.Processo_Numero and c.situacao = 'Sim' and p.`Localidade do Chamado_idLocalidade` = l.idLocalidade
                l.`rpa_id_rpa` = '''+a+''';'''


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

            pernambuco.add_child(plugins.HeatMap(lista3,min_opacity=0.7,max_val=0.5,))
            map_path = app.root_path + '/templates' + '/' + 'map_lonas.html'
            pernambuco.save(map_path)

        retorno = request.form.get("rpa_opcao")

        rpa1 = '1'
        rpa2 = '2'
        rpa3 = '3'
        rpa4 = '4'
        rpa5 = '5'
        rpa6 = '6'


        if retorno == rpa1:
            Calango(rpa1)
            return render_template('mapacalorlonas.html')
    
        if retorno ==rpa2:
            Calango(rpa2)
            return render_template('mapacalorlonas.html')
    
        if retorno == rpa3:
            Calango(rpa3)
            return render_template('mapacalorlonas.html')
    
        if retorno == rpa4:
            Calango(rpa4)
            return render_template('mapacalorlonas.html')
    
        if retorno == rpa5:
            Calango(rpa5)
            return render_template('mapacalorlonas.html')
    
        if retorno == rpa6:
            Calango(rpa6)
            return render_template('mapacalorlonas.html')
    
        if retorno == 'Todas':

            Calango(False)
            return render_template('mapacalorlonas.html')
    
    
    if request.method == "GET":

        conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
        c = conexao.cursor()
    

        consulta2 = '''SELECT `rpa_nome` ,count(`rpa_nome`) 
        from mydb_ufrpe.`sedecchamados` as c , mydb_ufrpe.sedeclonas as l 
        where c.processo_numero = l.processo_numero and l.colocacao_lona_situacao = "Sim" 
        GROUP BY `rpa_nome` '''

        c.execute(consulta2)
        re = c.fetchall()
        re2 =[]
        total = 0
        for x in re:
            total = x[1] + total

        for x in re:
            nomeRpa = x[0]
            qtdChamados = x[1]
            link = 'http://www2.recife.pe.gov.br/servico/sobre-rpa-' + nomeRpa[0]
            percentual = qtdChamados/total*100
            string = ("%.2f" % percentual)
            re2.append([nomeRpa, qtdChamados, link, string])
        re2.sort(reverse = True,key=lambda x:x[1])

        
    
        

        return render_template('mapalonasporrpa.html', rpa = re2)
    return render_template('mapalonasporrpa.html')

@app.route('/mcl')
def mcl():

    return render_template('map_lonas.html')

@app.route('/mcc')
def mcc():
    return render_template('map_test2.html')



@app.route("/mapaCalorVistoria")
def mapaCalorVistoria():
    conexao = pymysql.connect(host='www.db4free.net',user='alunoufrpe',password='ufrpe2018.2',db='mydb_ufrpe')
    c = conexao.cursor()
    consulta = ''' select Latitude,Longitude from `Localidade do Chamado` 
    where idLocalidade in(SELECT `Localidade do Chamado_idLocalidade` 
    FROM mydb_ufrpe.processo as p , mydb_ufrpe.vistoria as v where p.Numero = v.Processo_Numero); '''
    #consulta = '''SELECT `Latitude`, `Longitude` FROM `sedecvistorias` as vist, `sedecchamados` as chama WHERE vist.processo_numero = chama.processo_numero ;'''
    c.execute(consulta)
    resposta = c.fetchall()
    lista3=[]
    for x in resposta:
        try:
            lat = float(x[0])
            long = float(x[1])
            lista3.append([lat,long])

        except:
            pass



        consulta2 = '''SELECT `rpa_nome` ,count(`rpa_nome`) 
        from mydb_ufrpe.`sedecchamados` as c , mydb_ufrpe.vistoria as v 
        where c.processo_numero = v.processo_numero 
        GROUP BY `rpa_nome` '''

        c.execute(consulta2)
        re = c.fetchall()
        re2 =[]
        total = 0
        for x in re:
            total = x[1] + total

        for x in re:
            nomeRpa = x[0]
            qtdChamados = x[1]
            link = 'http://www2.recife.pe.gov.br/servico/sobre-rpa-' + nomeRpa[0]
            percentual = qtdChamados/total*100
            string = ("%.2f" % percentual)
            re2.append([nomeRpa, qtdChamados, link, string])
        re2.sort(reverse = True,key=lambda x:x[1])


    
    pernambuco = folium.Map(location=[-8.0421584, -35.008676],zoom_start=10)


    pernambuco.add_child(plugins.HeatMap(lista3,min_opacity=0.7,max_val=0.5,))


    pernambuco.add_child(plugins.HeatMap(lista3,min_opacity=0.7,max_val=0.5,))
    map_path = app.root_path + '/templates' + '/' + 'map_vistorias.html'
    pernambuco.save(map_path)


    return render_template ('mapaVistoria.html', resporta = rpa)


@app.route('/mcv')
def mcv():
    return render_template('map_vistorias.html')