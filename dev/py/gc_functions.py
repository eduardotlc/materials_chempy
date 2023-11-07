#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:05:23 2023

@author: eduardotc

[eduardotcampos@usp.br]
"""

from tkinter import Tk, filedialog   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from astropy import units as u
from specutils.spectra import Spectrum1D
from specutils.fitting import fit_lines
from distinctipy import get_colors
from spectrum_overload import Spectrum
import astropy
palette = get_colors((15), None, False, 0.6, 1000, None, None)
# rcp.['font.family'] = ['sans-serif', 'sans', 'times', 'serif', 'monospace', 'cursive']

font1 = {'family':"cursive","style": "italic",'color':'black','size':16,'name':"Cantarell"}
font3 = {'family':"serif","style": "italic",'color':'black','size':16, 'name':"DejaVuSerif-Italic"}
font4 = {'family':"sans","style": "italic",'color':'black','size':16, 'name':"DroidSans-Bold"}
font5 = {'family':"monospace","style": "italic",'color':'black','size':16, 'name':"LiberationMono-BoldItalic"}
font_n = font5
font_n2 = font1
font_n3 = font1



def create_subfolder():
    """
    Define o caminho para uma pasta pai, para futuramente juntar com o nome de unm arquivo e obter o path completo.
    
    Inputs
    ----------
    source_path : tkinter.string
        String com path de um arquivo, selecionado interativamente pelo GUI do tkinter

    Example
    -------
    >>> create_subfolder()
    subfolder created
    
    """
    source_path = filedialog.askdirectory(title='Diretório Pai da Imagem: ')
    path = os.path.join(source_path, 'Images')
    os.makedirs(path)

    
def file_path():
    """
    Definir o path de um arquivo interativamente, pelo tkinter.
    
    Input
    ----------
    askopenfilename() : tkinter
        Seleção de um arquivo, interativamente pelo GUI do tkinter
    
    Returns
    -------
    arquivo : string
        Path completo de um arquivo
    
    Exemplo
    -------
    >>>file = file_path()
    file: "/home/eduardo/Documentos/Resultados/AuNp.txt"
    
    """
    Tk().withdraw()
    arquivo = askopenfilename()
    return arquivo


def file_name(path):
    """
    Extrair o nome de um arquivo, dando o path dele como argumento.
    
    Parameters
    ----------
    path : string
        Path completo do arquivo que se deseja o nome.
    
    Returns
    -------
    name : string
        O nome do arquivo cujo path completo foi fornecido.
    
    Example
    -------
    >>> file_name("/home/home/eduardo/Documentos/teste.py")
    teste.py
    
    """
    name_list1 = path.split('/')
    name1 = name_list1[-1]
    name_list2 = name1.split('.')
    name2 = name_list2[0]
    name_list3 = name2.split("_")
    name = " ".join(name_list3)
    return name
    
   
def axis_xy(arquivo):
    """
    Separa um arquivo txt de emissão de fluorescência, em seus eixos x e y.
    
    Parâmetros
    ----------
    arquivo : string
        String com path do arquivo txt de emissão de fluorescência, que contém os eixos x e y
    
    Returns
    -------
    eixo_x : numpy.ndarray
        Lista contendo todos os pontos do eixo x
    
    eixo_y : numpy.ndarray
        Lista contendo todos os pontos do eixo_y
    
    Exemplo
    -------
    >>> eixo_x, eixo_y = axis_xy("/home/eduardo/Documentos/Resultados/AuNp.txt")
    eixo_x: [1200, 1201, 1202, 1203...]
    eixo_y: [870, 879, 887, 901...]
    
    """
    with open(arquivo) as file: 
        a = 2    # Inicialização da varíavel que será o contador para saber se o índice de um elemento da lista é par ou impar
        eixo_x = [] # Inicializar listas vazias aonde serão armazenados os valores dos eixos x e y
        eixo_y = []
        f = file.read()  #Lendo arquivo txt
        lista_global = f.split() #Criando uma lista que contém tanto eixo x quanto y, ainda juntos, tendo cada elemento sido separado por uma barra de espaço no arquivo txt original
        del lista_global[0:285]
        del lista_global[-7:]
    for n in lista_global: #Algoritmo aplicado em todos elementos da lista 
        if a % 2 == 0 : #Caso o índice do elemento seja par
            eixo_x.append(float(n)) #Adicionar a lista do eixo X
        else: #Caso o índice do elemento seja ímpar
            eixo_y.append(float(n)) 
        a = a + 1
    eixo_x = np.array(eixo_x)
    eixo_y = np.array(eixo_y)
    return eixo_x, eixo_y


def savegraph():
    """
    Salvar gráfico que foi plotado pelo matplotlib em arquivo png.
    
    Inputs
    ----------
    Nome do arquivo da imagem : Input string, iterno da função.
        Nome do arquivo salvo.
        
    folder_selected : String, interno da função.
        String com path da pasta que o arquivo será salvo.
    
    Returns
    -------
    savegraph : Arquivo de imagem png.
        Arquivo png com o gráfico das curvas plotadas.
    
    Exemplo
    -------
    >>> savegraph()
    Arquivo.png é salvo em uma pasta escolhida.
    
    """
    name_to_save = str(input("Nome do árquivo de imagem: "))
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    local = folder_selected + "/" + name_to_save
    plt.savefig(local, dpi = 800)
    return savegraph


def fit_spectra(eixo_x, eixo_y, baseline, w1, w2, titulo_norm, nciclos):
    """
    Normalização de uma curva de emissão de fluorescência, adaptando ela a uma distribuição gaussiana.
    
    Parâmetros
    ----------
    x : list
        Lista/array contendo os valores do eixo x
        
    y : list
        Lista/array contendo os valores do eixo y
        
    baseline : float
        Valor da baseline (aproximada) da curva de emissão sem tratamento, plotada anteriormente
        
    w1 : float
        Limite inferior, dos valores do eixo x, que serão normalizados
        
    w2 : float
        Limite superior, dos valores do eixo x, que serão normalizados
        
    titulo_norm : string
        Titulo do gráfico normalizado, extraido através da função de plotagem sem normalizar
        
    nciclos : integer
        Fornecido pela função draw_graph, contador de quantas curvas ja foram plotadas
    
    Returns
    -------
    fig
        Figura plotada pelo matplotlib
    
    Exemplo
    -------
    >>> eixo_ynorm = fit_spectra(eixo_x, eixo_y, 400, 1200, 1300)
    eixo_ynorm: [array normalizada]
    
    Customização
    ------------
    stddev : float
        Desvio padrão da curva normalizada
    
    """  
    maxpos = eixo_y.argmax()
    maxpos = maxpos + eixo_x[0]
    amp = eixo_y.max() - baseline
    spectrum = Spectrum1D(flux=eixo_y*(u.ct/u.s), spectral_axis=eixo_x*u.nm)
    g_init = models.Gaussian1D(amplitude=amp*(u.ct/u.s), mean=maxpos*u.nm, stddev=0.2*u.nm)
    g_fit = fit_lines(spectrum, g_init, window=(w1*u.nm, w2*u.nm))
    y_fit = g_fit(eixo_x*u.nm)
    fig,ax = plt.subplots()
    ax.plot(eixo_x, y_fit, color = palette[nciclos])
    ax.set_xlabel("Wavelength (nm)", )
    ax.set_ylabel("CPS")
    ax.grid()
    return fig


def draw_graph():
    """
    Plotar gŕafico de emissão de fluorescência de medidas.
    
    Inputs
    ----------
    ngraficos : integer
        Número total de curvas/medidas que devem ser plotadas.
        
    titulo : string
        Titulo do gráfico contendo todas as curvas plotadas, caso ngraficos=1 não precisa ser inserido.
    
    font_n : integer
        número da fonte, do dicionário pré estabelecido de fontes, da figura
        
    Returns
    -------
    fig : numpy graph
        Gráfico plotado pelo matplotlib
      
    eixo_x : numpy.ndarray
        array com valores do eixo x
        
    eixo_y : numpy.ndarray
        array com os valores do eixo y
        
    titulo_norm : string
        Titulo do grafico normalizado, para caso o normalizado seja plotado, não ser necessário inserir o título novamente por arquivo
    
    arquivo : string
        String contendo o path do arquivo txt que será aberto, é retornado para utilizar novamente na plotagem do gráfico normalizado
        
    nciclos : integer
        Contador que marca quantas curvas ja foram plotadas
        
    Exemplo
    -------
    >>> fig, eixo_x, eixo_y, titulo_norm, arquivo, n_ciclos = draw_graph()
    Gŕafico de emissão de fluorescência
    Valores atribuidos a todos os argumentos de retorno
    
    Customização
    ------------
    fontname : Dictionary
        Variável referente as fontes, em forma de dicionário, presentes no começo do arquivo
        
    
    """
    ngraficos = int(input("Número de gráficos a serem plotados: "))
    nciclos = 0
    titulo = False
    fig,ax = plt.subplots()
    if ngraficos > 1:
        titulo = str(input("Titulo do gráfico.\n"))
    while ngraficos > nciclos:
        arquivo = file_path()
        eixo_x, eixo_y = axis_xy(arquivo)
        filename = file_name(arquivo)
        if not titulo:
            titulo = filename
        ax.plot(eixo_x, eixo_y, label = "%s" %filename, color = palette[nciclos])
        nciclos = nciclos + 1
    ax.set_title(titulo)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("CPS") 
    ax.legend()
    titulo_norm = (("%s Normalizado" % titulo) )
    return fig, eixo_x, eixo_y, titulo_norm, arquivo, nciclos
    
def norm_spec_overload(eixo_x, eixo_y, method, deg, titulo_norm, nciclos):
    """
    Normalizar o gráfico através de integração com o módulo spectrum_overload
    
    Inputs
    ----------
    eixo_x : np.array
        Eixo x do gráfico que será tratado.
        
    eixo_y : np.array
        Eixo y do gráfico que será tratado.

    method : string
        Escolher entre os métodos de normalização disponíveis, que são scalar, linear, quadratic, cubic, poly and exponential
        
    deg : integer
        Grau polinomial do método poly, padrão é 0
        
    titulo_norm : string
        Titulo do gráfico normalizado, obtido ja na função que plotou o gráfico sem normalização
        
    nciclos : integer 
        Contador de quantos gráficos ja foram plotados, para controlar o número correspondente a cor do gráfico
        
        
        
    Returns
    -------
    norm_spec : Spectrum
        Conjunto de arrays do espectro normalizado, que pode fornecer os eixos do mesmo caso necessário, pelas funções .xaxis e .flux
        
   nciclos : integer 
       Contador de quantos gráficos ja foram plotados, para controlar o número correspondente a cor do gráfico
        
    Exemplo
    -------
    >>> a, b = norm_spec_overload(eixo_x, eixo_y, quadratic, 0, titulo_norm, nciclos)
    a: Spectrum
    b: nciclos
    *Gráfico normalizado é plotado*
        
    """
    normover=Spectrum(flux=eixo_y, xaxis=eixo_x)
    if method == "poly":
        normover2=normover.normalize(method="%s" %method, degree=deg)
    else:
        normover2=normover.normalize(method="%s" %method)
    normover_x = normover2.xaxis
    normover_y = normover2.flux
    subfig,ax = plt.subplots()
    ax.plot(normover_x, normover_y, label="%s"%method, color=palette[nciclos])
    nciclos = nciclos + 1
    ax.set_title(titulo_norm)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("CPS")
    ax.legend()
    return normover2, nciclos