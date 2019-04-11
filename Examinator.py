
#Trabalho algoritimos 2
#Python 3.7.0
from math import trunc

arq = open('C:\Algo2\TrabAlgo2\casos\CasoDev.txt', 'r')
pergaminho = arq.readlines()

def terras(pergaminho):
    """
    :param pergaminho: pergaminho a ser lido
    :return: string com o valor da primeira terra a ser dividida
    """
    terras = pergaminho[0]
    return terras


#quebrando o pergaminho em pequenas sublistas:
def sublistas(pergaminho):
    """
     Função para quebrar o pergaminho em sublistas de três elementos
    :param pergaminho: pergaminho a ser "quebrado"
    :return: retorna uma lista com sublistas, na ordem: pai, filho e quant de terras
    """
    x = []
    y = []
    for i in range(len(pergaminho)):
        y.append(pergaminho[i])
        x.append(y[i].split())
    del(x[0])
    return x

def primeiro_pai(sub_pergaminho):
    """
    :param pergaminho: sub_pergaminho a ser lido
    :return: String com o nome do primeiro pai
    """
    lista1 = []
    lista2 = []
    for i in range(len(sub_pergaminho)):
        lista1.append(sub_pergaminho[i][1]) #extraindo filhos
        lista2.append(sub_pergaminho[i][0]) #extraindo pais
    lista_final = list(set(lista2) - set(lista1)) #retirando o primeiro pai
    return lista_final[0]


def contagem(pai,sub_pergaminho):
    cont = 0
    for i in range(len(sub_pergaminho)):
        if pai in sub_pergaminho[i]:
            cont += 1
    return cont


def dic_organizator(sub_pergaminho,pai):
    dicionario = {}
    count = 0
    for i in range(len(sub_pergaminho)):
        if pai == sub_pergaminho[i][0] and count == 0:
            lista = []
            dicionario[sub_pergaminho[i][0]] = lista
            dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][1])
            dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][2])
            pai = sub_pergaminho[i][0]
            count = 1

        elif pai != sub_pergaminho[i][0]:
            if sub_pergaminho[i][0] in dicionario:
                dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][1])
                dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][2])
                pai = sub_pergaminho[i][0]
            else:
                lista = []
                dicionario[sub_pergaminho[i][0]] = lista
                dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][1])
                dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][2])
                pai = sub_pergaminho[i][0]

        else:
            if pai in dicionario:
                dicionario[pai].append(sub_pergaminho[i][1])
                dicionario[pai].append(sub_pergaminho[i][2])
                pai = sub_pergaminho[i][0]

    return dicionario


def dicionario_valores_somados(pai,terras2,dicionario):
    terras = terras2
    lista_pais = list(dicionario.keys())
    lista_filhos = list(dicionario.values())
    print('inicio:')
    print(lista_pais)
    print(lista_filhos)
    x = 1
    contagem = trunc(len(lista_filhos[0])/2)
    valor_para_somar = trunc((int(terras) / int(contagem)))
    for k, v in dicionario.items():
        print(k)
        if k == lista_pais[0]:
            valor = int(v[x])
            valor = valor + valor_para_somar
            v[x] = str(valor)
            x += 2
            print('oi'+ str(x))


    print(dicionario)







#extraindo uma listas com sublistas do pergaminho:
sub_pergaminho = sublistas(pergaminho)

#extraindo o primeiro pai e a quantidade de terras:
pai = primeiro_pai(sub_pergaminho)
terras = terras(pergaminho)

#extraindo a contagem para a divisão de terras do primeiro pai
contagem = (contagem(pai,sub_pergaminho))

#extraindo o dicionario:
dicionario = (dic_organizator(sub_pergaminho,pai))


print(pai)
print(terras)
print(contagem)
print(sub_pergaminho)
print(dicionario)

dicionario_valores_somados(pai,terras,dicionario)

