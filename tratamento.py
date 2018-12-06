from app import app
with open('sedecvistorias2.csv', "rb") as ifile:
    read = csv.reader(codecs.iterdecode(ifile, 'utf-8'),delimiter=';')
    for row in read :
        if row[0] =='ano':
            continue
        else:
            passarParaBdVistoria(row)
            
    with open('sedectipoocorrencias.csv', "rb") as ifile:
        read = csv.reader(codecs.iterdecode(ifile, 'utf-8'),delimiter=';')
        for row in read :
            if row[0] =='processo_numero':
                continue
            else:
                passarParaBdTipodeOcorrencia(row)
        

    with open('sedecchamados.csv', "rb") as ifile:
        read = csv.reader(codecs.iterdecode(ifile, 'utf-8'),delimiter=';')
        for row in read :
            if row[0] =='ano':
                continue
            else:
                passarParaBdChamados(row)


    with open('sedeclonas.csv', "rb") as ifile:
        read = csv.reader(codecs.iterdecode(ifile, 'utf-8'),delimiter=';')
        for row in read :
            if row[0] =='ano':
                continue
            else:
                passarParaBdLonas(row)

    with open('sedecSolicitacao.csv', "rb") as ifile:
        read = csv.reader(codecs.iterdecode(ifile, 'utf-8'),delimiter=';')
        for row in read :
            if row[0] =='ano':
                continue
            else:
                passarParaBdSolicitacao(row)

def passarParaBdVistoria(tripla):

    ano = int(tripla[0])
    mes = int(tripla[1][:2])
    avaliador = tripla[2]
    vistoriaData = tripla[3]
    vistoriaRisco = tripla[4]
    vistoriaLocalidade = tripla[5]
    vistoriaRpa = int(tripla[6])
    vistoriaMicroregiao = float(tripla[7])
    vistoriaSetor = tripla[8]
    processoNumero = int(tripla[9])

    #lista=[ano,mes,avaliador,vistoriaData,vistoriaRisco,vistoriaLocalidade,vistoriaRpa,vistoriaMicroregiao,vistoriaSetor,processoNumero]

def passarParaBdTipodeOcorrencia(tripla):

    processo = int(tripla[0])
    processo_ocorrencia = tripla[1]


def passarParaBdChamados(tripla):

    ano = int(tripla[0])
    mes = int(tripla[1])
    processoNumero = int(tripla[2])
    solicitacaoData = tripla[3]
    solicitacaoDescricao = tripla[4]
    solicitacaoRegional = tripla[5]
    solicitacaoBairro = tripla[6]
    solicitacaoLocalidade = tripla[7]
    solicitacaoEndereco = tripla[8]
    solicitacaoRoteiro = tripla[9]
    rpaCodigo = int(tripla[10])
    rpaNome = tripla[11]
    solicitacaoMicrorregiao = tripla[12]
    solicitacaoPlantao = tripla[13]
    solicitacaoOrigemChamado = tripla[14]
    latitude = float(tripla[15])
    longitude = float(tripla[16])
    solicitacaoVitima = tripla[17]
    solicitacaoVitimasFatais = tripla[18]
    processoSituacao = tripla[19]
    processoTipo = tripla[20]
    processoOrigem = tripla[21]
    processoLocalizacao = tripla[22]
    processoStatus = tripla[23]
    processoDataConclusao = tripla[24]
    
def passarParaBdLonas(tripla):

    ano = int(tripla[0])
    mes = int(tripla[1])
    processoNumero = int(tripla[2]) 
    colocacaoLonaSituacao = tripla[3]
    colocacaoLonaData = tripla[4]
    colocacaoLonaJustificativa = tripla[5]
    colocacaoLonaMetragem = int(tripla[6])
    colocacaoQuantidadePontos = int(tripla[7])
    
def passarParaBdSolicitacao(tripla):
    ano = int(tripla[0])
    mes = int(tripla[1])
    processo_numero = int(tripla[2])
    solicitacao_data = int(tripla[3])
    solicitacao_hora = int(tripla[4])
    solicitacao_descricao = tripla[5]
    solicitacao_regional = tripla[6]
    solicitacao_bairro = tripla[7]
    solicitacao_localidade = tripla[8]
    solicitacao_endereco = tripla[9]
    solicitacao_roteiro = tripla[10]
    rpa_codigo = int(tripla[11])
    rpa_nome = tripla[12]
    solicitacao_microrregiao = tripla[13]
    solicitacao_plantao = tripla[14]
    processo_situacao = tripla[15]
    processo_tipo = tripla[16]
    processo_origem = tripla[17]
    processo_solicitacao = tripla[18]
