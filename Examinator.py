
#Trabalho algoritimos 2
#Python 3.7.0

arq = open('C:\Algo2\TrabAlgo2\casos\casoDev.txt', 'r')
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


#extraindo uma listas com sublistas do pergaminho:
sub_pergaminho = sublistas(pergaminho)

#extraindo o primeiro pai e a quantidade de terras:
pai = primeiro_pai(sub_pergaminho)
terras = terras(pergaminho)




print(pai)
print(terras)
print(sub_pergaminho)
print(contagem(pai,sub_pergaminho))

