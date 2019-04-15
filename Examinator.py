#Trabalho algoritimos 2
#Python 3.7.0
from math import trunc
import collections
import time


arq = open('/home/henrique/algo2/TrabAlgo2/casos/casoMC4a.txt', 'r')
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
    :param sub_pergaminho: lista a ser lida
    :return: class 'collections.OrderedDict
    """
    dicionario = collections.OrderedDict()
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


def dicionario_valores(pai,terras,dicionario):
   """
   Função que retorna um OrderedDict com os valores das terras dos filhos somados
   :param pai: nome do primeiro pai
   :param terras: a quantidade de terras do primeiro pai
   :param dicionario: OrderedDict a ser lido
   :return: class 'collections.OrderedDict
   """
   x = 0 
   y = 0
   z = 0
   count = 0
   pos = 0
   chave = ''
   chave_pai = ''
   lista_pais = list(dicionario.keys())
   lista_filhos = list(dicionario.values())
   for i in range(len(lista_pais)):
      contagem = trunc(len(lista_filhos[i])/2)
      if count == 0:
          terras = terras
          count  = 1
          
      else:
          for i in range(len(lista_filhos)):
              if lista_pais[x] not in lista_filhos[i]:
                 
                  pass
        
              else:
                  #pegando a posição do nome do pai
                  pos = (lista_filhos[i].index(lista_pais[x]))
                  pos = pos+1 #(pos == nome, pos +1 == terras)
                  chave = lista_pais[x]
                  break
           
          #procurando pai da chave:
          for k,v in dicionario.items():
              if chave in v:
                 chave_pai = k
                  
          #pegando o valor das terras do dicionario
          terras = dicionario[chave_pai][pos]
      x += 1
      
      #percorrendo todos os filhos e atualizando os valores
      valor_para_somar = trunc((int(terras) / int(contagem)))
      value = len(lista_filhos[z])
      for i in range(1,value,2):
          valor = int(dicionario[lista_pais[y]][i])
          valor = valor + valor_para_somar
          dicionario[lista_pais[y]][i] = str(valor)
          terras = 0
      y += 1
      z += 1
      #reinicia o loop do primeiro for 
   return dicionario



def busca_guerreiro(dicionario_pronto):
    
    lista = []
    maior = 0
    filhos = []
    ocara = ''
    lista_filhos = list(dicionario_pronto.values())
    lista_pais = list(dicionario.keys())
    #obtendo a lista com o máximo  das ultimas gerações    
    for i in range(len(lista_pais)):
        value = len(lista_filhos[i])
        for j in range(1,value,2):
            lista.append(int(lista_filhos[i][j])) #lista valores, convertidos para inteiros
            maior = max(lista) # variavel com o maior valor de terras
            
    #pegando a lista que contém do valor maior:
    for k,v in dicionario_pronto.items():
       if str(maior) in v:
           filhos = v
           
    #pegando o nome do guerreiro
    for i in range(len(filhos)):
        if str(maior) in filhos[i]:
            ocara = filhos[i-1]
            
            
    return '\nO filho com maior quantidade de terras é o {} ({})\n'.format(ocara,maior)
    
  
   
    
 
if __name__ == "__main__":
         
    inicio=time.time()
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
    dicionario_pronto = dicionario_valores(pai,terras,dicionario)

    print(busca_guerreiro(dicionario_pronto))
    
    print("Quantidade inicial: {}".format(terras))
    
    fim=time.time()
    
    print("Tempo total: {} milisegundos".format(fim-inicio))





