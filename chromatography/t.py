# -*- coding: ISO-8859-1 -*-
"""
Created on Sat Mar  4 07:38:23 2023.

@author: eduardo
"""
import numpy as np
def teste(arquivo):
    with open(arquivo) as file:
        a = 2    # Inicialização da varíavel que será o contador para saber se o índice de um elemento da lista é par ou impar
        eixo_x = [] # Inicializar listas vazias aonde serão armazenados os valores dos eixos x e y
        eixo_y = []
        f = file.read()  #Lendo arquivo txt
        lista_global = f.split() #Criando uma lista que contém tanto eixo x quanto y, ainda juntos, tendo cada elemento sido separado por uma barra de espaço no arquivo txt original
        del lista_global[0:285]
        del (lista_global[-7:])
        for n in lista_global: #Algoritmo aplicado em todos elementos da lista
            if a % 2 == 0 : #Caso o índice do elemento seja par
                eixo_x.append(float(n)) #Adicionar a lista do eixo X

            else: #Caso o índice do elemento seja ímpar
                eixo_y.append(float(n))
            a = a + 1
        eixo_x = np.array(eixo_x)
        eixo_y = np.array(eixo_y)
        return eixo_x, eixo_y


tst = teste("/home/eduardo/Data/GC/9-10DBA_DCM_1.TXT")
print (tst)