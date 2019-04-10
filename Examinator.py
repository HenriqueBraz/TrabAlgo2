
#Trabalho algoritimos 2
#Python 3.7.0

arq = open('/home/luis/Documentos/pucrs/alest/TrabAlgo2/casos/CasoDev.txt', 'r')
pergaminho = arq.readlines()
print(pergaminho)


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
    return sub_pergaminho[0][0]

def contagem(pai,sub_pergaminho):
    cont = 0
    for i in range(len(sub_pergaminho)):
        if pai in sub_pergaminho[i]:
            cont += 1
    return cont


def dic_organizator(sub_pergaminho,pai2):
    dicionario = {}
    pai = pai2
    count = 0
    for i in range(15):
        if pai == sub_pergaminho[i][0] and count == 0:
            lista = []
            dicionario[sub_pergaminho[i][0]] = lista
            dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][1])
            dicionario[sub_pergaminho[i][0]].append(sub_pergaminho[i][2])
            pai = sub_pergaminho[i][0]
            print(pai+" do if")
            count = 1

        elif pai != sub_pergaminho[i][0]:
            print(pai + " do elif")
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
                print(pai +" do else")

    return dicionario




#extraindo uma listas com sublistas do pergaminho:
sub_pergaminho = sublistas(pergaminho)

#extraindo o primeiro pai e a quantidade de terras:
pai = primeiro_pai(sub_pergaminho)
terras = terras(pergaminho)

#extraindo a contagem para a divisão de terras do primeiro pai
contagem = (contagem(pai,sub_pergaminho))


print(pai)
print(terras)
print(sub_pergaminho)
print(contagem)

print(dic_organizator(sub_pergaminho,pai))


