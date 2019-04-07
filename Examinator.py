
#Trabalho algoritimos 2
#Python 3.7.0

arq = open('C:\Algo2\TrabAlgo2\casos\casoDev.txt', 'r')
pergaminho = arq.readlines()
print(pergaminho)


def primeiro_pai(pergaminho):
    """
    :param pergaminho: pergaminho a ser lido
    :return: String com o nome do primeiro pai
    """
    lista1 = pergaminho[1]
    lista2 = lista1.split()
    x = [lista2[0]]
    pai = x[0]
    return pai

def terras(pergaminho):
    """
    :param pergaminho: pergaminho a ser lido
    :return: string com o valor da primeira terra a ser dividida
    """
    terras = pergaminho[0]
    return terras


#extraindo o primeiro pai e a quantidade de terras:
pai = primeiro_pai(pergaminho)
terras = terras(pergaminho)


#quebrando o pergaminho em pequenas sublistas:
def sublistas(pergaminho):
    x = []
    y = []
    for i in pergaminho:
        x += ['']
    for i in range(len(pergaminho)):
        y.append(pergaminho[i])
        x[i] = y[i].split()
    del(x[0])
    return x

print(pai)
print(terras)
print(sublistas(pergaminho))


