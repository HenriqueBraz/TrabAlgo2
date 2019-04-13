#Trabalho algoritimos 2
#Python 3.7.0
from math import trunc
import collections


arq = open('/home/henrique/algo2/TrabAlgo2/casos/CasoDev.txt', 'r')
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
    """
    Função que retorna a quantidade de pais no sub_pergaminho
    :param sub_pergaminho: sub_pergaminho a ser lido
    :return: Int com o numero de pais
    """
    cont = 0
    for i in range(len(sub_pergaminho)):
        if pai in sub_pergaminho[i]:
            cont += 1
    return cont


def dic_organizator(sub_pergaminho,pai):
    """
    Função que retorna um dicionario ordenado por ordem de inserção
    :param pai: nome do primeiro pai
    :param sub_pergaminho: sub_pergaminho a ser lido
    :return: class 'collections.OrderedDict
    """
    dicionario = collections.OrderedDict()
    count = 0
    for i in range(len(sub_pergaminho)):
        if pai == sub_pergaminho[i-1][0] and count == 0:
            lista = []
            dicionario[sub_pergaminho[i][0]] = lista
            dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][1])
            dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][2])
            pai = sub_pergaminho[i][0]
            count = 1

        elif pai != sub_pergaminho[i][0]:
            if sub_pergaminho[i][0] in dicionario:
                pai = sub_pergaminho[i][0]
                dicionario[pai].append(sub_pergaminho[i][1])
                dicionario[pai].append(sub_pergaminho[i][2])
                
            else:
                lista = []
                pai = sub_pergaminho[i][0]
                dicionario[pai] = lista
                dicionario[pai].append(sub_pergaminho[i][1])
                dicionario[pai].append(sub_pergaminho[i][2])
                

        else:
            if pai in dicionario:
                dicionario[pai].append(sub_pergaminho[i][1])
                dicionario[pai].append(sub_pergaminho[i][2])
                           
    return dicionario


def dicionario_valores_somados(pai,terras2,dicionario):
    """
    Função que retorna um OrderedDict com os valores das terras dos filhos somados
    :param pai: nome do primeiro pai
    :param dicionario: OrderedDict a ser lido
    :return: class 'collections.OrderedDict
    """
    x = 0
    y = 0
    terras = terras2
    lista_pais = list(dicionario.keys())
    lista_filhos = list(dicionario.values())
    print('***** inicio: ******')
    print(lista_pais)
    print(lista_filhos)
    for i in dicionario.keys():
        contagem = trunc(len(lista_filhos[x])/2)
        valor_para_somar = trunc((int(terras) / int(contagem)))
        value = len(dicionario[lista_pais[y]])
        for i in range(1,value,2):
            valor = int(dicionario[lista_pais[y]][i])
            valor = valor + valor_para_somar
            dicionario[lista_pais[y]][i] = str(valor)
            terras = 0
            x += 1
            y += 1
            print('*')
            

    print(dicionario)
    print(valor_para_somar)



#extraindo uma listas com sublistas do pergaminho:
sub_pergaminho = sublistas(pergaminho)

#extraindo o primeiro pai e a quantidade de terras:
pai = primeiro_pai(sub_pergaminho)
terras = terras(pergaminho)

#extraindo a contagem para a divisão de terras do primeiro pai
contagem = (contagem(pai,sub_pergaminho))

#extraindo o dicionario:
dicionario = (dic_organizator(sub_pergaminho,pai))


#dicionario pronto:
dicionario_valores_somados(pai,terras,dicionario)


print(pai)
print('\n')
print(terras)
print('\n')
print(contagem)
print('\n')
print(sub_pergaminho)
print('\n')
print(dicionario)



