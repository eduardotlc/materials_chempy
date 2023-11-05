r"""°°°
# References
---
---


## GC_Functions
---
°°°"""
# |%%--%%| <qjjIQEw13V|K8fJAn8Zcl>

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 07:38:23 2023.

@author: eduardo
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

# |%%--%%| <K8fJAn8Zcl|46jKy1AH1K>
r"""°°°
<br>


## ASCII plots
---

°°°"""
# |%%--%%| <46jKy1AH1K|7IXmuLSbgz>

#!/usr/bin/nv python
# -*- coding: utf-8 -*-

"""
[eduardotcampos@usp.br
[07/15/23 : 6:25 AM]
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy as np
from distinctipy import get_colors
import csv
from specutils import Spectrum1D

# Defining dictionary of fonts, to be used in the matplotlib functions like axes and titles, font names based on available downloaded system fonts,
# able to see them by: matplotlib.font_manager.get_font_names()
# matplotlib.font_manager.findSystemFonts(fontpaths = None, fontext = 'ttf')
fontdict = {"default_axis_normal": {'name': 'Droid Sans', 'color': 'black', 'weight': 'normal', 'size': 16}, "default_title_normal": {'name': 'Liberation '
'Mono', 'color': 'black', 'weight': 'bold', 'size': 19}, "default_axis_dark": {'name': 'Droid Sans', 'color': 'white', 'weight': 'normal', 'size': 16},
"default_title_dark":{'name': 'Liberation' 'Mono', 'color': 'white', 'weight': 'bold', 'size': 19}}



def palette(pastel, ncolors):
    """
    Defines the color palette that will be used to plot the graphs

    Inputs
    ----------
    pastel : float 0 ? 1
        Float representing how much "pastel" will be the colors used in the plots

    n_colors : integer
        number of colors that will be returned on the list

    Returns
    -----------
    palette : list
        A list of (r,g,b) colors that are visually distinct to each other

    Example
    -------
    >>> palette(0.8, 3)
    ([0,653,422],[133,444,111],[227,0,264])

    """
    # noinspection PyShadowingNames
    palette = get_colors(ncolors, None, False, pastel, 1000, None, None)
    return palette


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
    arquivo = askopenfilename(initialdir = "/home/eduardo/Data")
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


# noinspection DuplicatedCode
def axis_xy_fl(arquivo):
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
    >>> eixo_x, eixo_y = axis_xy_fl("/home/eduardo/Documentos/Resultados/AuNp.txt")
    eixo_x: [1200, 1201, 1202, 1203...]
    eixo_y: [870, 879, 887, 901...]
    
    """
    with open(arquivo, "r") as file:
        a = 2                        # Initialization of variable to be used as counter, to know if the list element is odd or even
        eixo_x = []                  # Initialize empty lists to be used in the storage of axis x and y
        eixo_y = []
        f = file.read()              # Reading ASCII .txt file
        lista_global = f.split()     # Creating a list that contains both axis elements, being the elements originally delimited from each-other by a space bar.
        del lista_global[:2]
    for n in lista_global:           # Algorithm applied to all list elements
        if a % 2 == 0:               # Case the list index is odd
            eixo_x.append(float(n))  # Appends the element to the x-axis list
        else:                        # Case the element index is even
            eixo_y.append(float(n))
        a = a + 1
    eixo_x = np.array(eixo_x)
    eixo_y = np.array(eixo_y)
    return eixo_x, eixo_y


# noinspection DuplicatedCode
def axis_xy_gc(arquivo):
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
    >>> eixo_x, eixo_y = axis_xy_fl("/home/eduardo/Documentos/Resultados/AuNp.txt")
    eixo_x: [1200, 1201, 1202, 1203...]
    eixo_y: [870, 879, 887, 901...]

    """
    with open(arquivo, 'r', encoding = "ISO-8859-1") as file:
        a = 0                                           # Initialization of variable to be used as counter, to know if the list element is odd or even
        eixo_x = []                                     # Initialize empty lists to be used in the storage of axis x and y
        eixo_y = []
        f = file.read()                                 # Reading ASCII .txt file
        lista_global = f.split()                        # Creating a list that contains both axis elements, being the elements originally delimited from/
                                                        # \ each-other by a space bar.
        datalim1 = lista_global.index("Intensity") + 1  # Finding the index of the word intensity in the file, last word before starting the plot data
        del lista_global[:datalim1]                     # Removing all elements befora the index found
        datalim2 = lista_global.index("[Chromatogram")  # Finding the index of the word [Chromatogram", the first word after ending the plot data
        del lista_global[datalim2:len(lista_global)]    # Removing all elements from the index found to the end of the file (length of the list)
        for n in lista_global:                              # Algorithm applied to all list elements
            if a % 2 == 0:                                  # Case the list index is odd
                eixo_x.append(float(n))                     # Appends the element to the x-axis list
            else:                                           # Case the element index is even
                eixo_y.append(float(n))
            a = a + 1
        eixo_x = np.array(eixo_x)
        eixo_y = np.array(eixo_y)
    return eixo_x, eixo_y


def draw_graph(palettes, plot_type, dictflargs):
    """
    Plot a 2d ASCII based graph. To work properly, the function palette has to have being called and defined to the variable palettes, and dictflargs has to
    be called to define user input cvalues, or define the predefined variables present in the function

    Inputs
    ----------
    palettes  :  List
        rgb list of colors to be used in the plots

    plot_type  :  string
        obtained internally in the function dictflargs, that defines which type of graph is being plotted
        possibilities: gc, fl

    dictflargs  :  Dictionary
        containing all the user input values, or default values in case the user don't input, used in this function to obtain the fonts of the
        plot axis labels adn title

    Returns
    -------
    eixo_x : numpy.ndarray
        array with x-axis values
        
    eixo_y : numpy.ndarray
        array with y-axis values
        
    titulo_norm : string
        Title of the normalized plot, to be used in case of later normalize function use
    
    arquivo : string
        with the ASCII file, to be used in case of later normalize function use
        
    nciclos : integer
        Counter that indicates how many plotting loops have already happened
        
    Exemplo
    -------
    # >>> fig, eixo_x, eixo_y, titulo_norm, arquivo, n_ciclos = draw_graph()
    Figure of the plotted values
    respectivities variables have their values defined

    """
    ngraficos = int(input("Número de gráficos a serem plotados: "))
    nciclos = 0
    # Defining the font to be used dictionary, by first extracting the name of the font from dictflargs dictionary, and them attributing this name to it
    # respective dictionary value in the predefined fontdict
    fontmyxy = dictflargs["fontxy"]
    fontmytitle = dictflargs["fonttitle"]
    fontmyxy = fontdict[("%s" % fontmyxy)]
    fontmytitle = fontdict[("%s" % fontmytitle)]
    # Starting a subplot function, permitting the plot of different subplots functions in the same figure
    fig, ax = plt.subplots()
    plt.figure(dpi = 800)
    plt.style.use('dark_background')
    # If more than 1 plot will be parsed, the title has to be interactive defined by the user, instead of based in the chosen txt file
    # Starting the plotting of the interactive chosen file loop, until the desired number of plots is equal to the times the loop has happened
    while ngraficos > nciclos:
        # Obtaining the file path interactively, with tkinter
        arquivo = file_path()
        filename = file_name(arquivo)
        # If the user chooses the file is a fluorescence emission
        if plot_type == "fl":
            eixo_x, eixo_y = axis_xy_fl(arquivo)
        # If the user chooses it is a shimadzu gas chromatography file
        elif plot_type == "gc":
            eixo_x, eixo_y = axis_xy_gc(arquivo)
        # plotting the defined axis in the figure
        # noinspection PyUnboundLocalVariable
        ax.plot(eixo_x, eixo_y, label = "%s" % filename, color = palettes[nciclos])
        # Counter of how many cycles have already being done
        nciclos = nciclos + 1
    # Defining some properties of the graph
    if ngraficos > 1:
        titulo = str(input("Titulo do gráfico.\n"))
        ax.legend()
    else:
        # noinspection PyUnboundLocalVariable
        titulo = filename
    if plot_type == "gc":
        ax.set_xlabel("Retention time (min)", fontdict = fontmyxy)
        ax.set_ylabel("Intensity", fontdict = fontmyxy)
    elif plot_type == "fl":
        ax.set_xlabel("Wavelength (nm)", fontdict = fontmyxy)
        ax.set_ylabel("CPS", fontdict = fontmyxy)
    ax.set_title(titulo, fontdict = fontmytitle)
    titulo_norm = ("%s Normalizado" % titulo)
    # noinspection PyUnboundLocalVariable
    return eixo_x, eixo_y, titulo_norm, arquivo, nciclos


def extract_last_row():
    """
    Extract the data, in float, of the last column in a .csv file

    Interactive inputs  : string
    ----------
    Path to a ASCII file, chosen interactively with tkinter

    Returns
    -------
    last_column : np.array[floats]
        numpy array containing the values extracted from the last column

    Example
    -------
    #>>> last_values = extract_last_row()
    #>>> input == Interactive tkinter path to the file
    [15.214, 15.782, 16.876, 16.990]


    """
    # Open the CSV file in read mode
    arquivo = file_path()
    with open(arquivo, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Initialize an empty list to store the values in the last column
        last_column = []

        # Loop through each row in the CSV file
        for row in reader:

            # Get the value in the last column of the row
            value = row[-1]

            # Try to convert the value to a float
            try:
                float_value = float(value)
            except ValueError:
                # If the value cannot be converted to a float, skip this row
                continue

            # Append the float value to the list
            last_column.append(float_value)

        # Print the values in the last column
        last_column = np.array(last_column)
        # x_column = np.arange(1, (len(last_column)+1), 1)
        return last_column


def plot_distribution(dictflargs, palettes):
    """
    Plot the histogram of distribution particles inside the function.

    Inputs
    ----------
    dictflargs  :  list
        List, with string elements extracted from user interactive input, from which the arguments for the function will be extracted

    palettes  :  List
        rgb list of colors to be used in the plots

    Arguments extracted from dictflargs
    ----------
    lim_min  :  float
        Inferior limit of the histogram bin, obtained by the interactive input arguments in dictflargs

    lim_max  :  float
        Superior limit of the histogram bin, obtained by the interactive input arguments in dictflargs

    interval  :  float
        Interval between the values of the bin, obtained by the interactive input arguments in dictflargs

    Returns
    -------
    histogram : numpy graph
        Numpy histogram plotted figure


    Example
    -------
    >>> plot_distribution(0, 40, 5)
    Histogram with y values defined by interactive tkinter selection, and bin from 0 to 40, with the values separated by 5

    """
    lim_min = dictflargs["lim_min"]
    lim_max = dictflargs["lim_max"]
    interval = dictflargs["interval"]
    fontmyxy = dictflargs["fontxy"]
    fontmytitle = dictflargs["fonttitle"]
    fontmyxy = fontdict[("%s" % fontmyxy)]
    fontmytitle = fontdict[("%s" % fontmytitle)]
    last_column = extract_last_row()
    bin = np.arange(lim_min, lim_max, interval)
    plt.style.use('dark_background')
    plt.figure(dpi = 800)
    fig, ax = plt.subplots()
    histogram = ax.hist(last_column, bin,  color = palettes[0], density=True)
    ax.set_xlabel("particle size (nm)", fontdict = fontmyxy)
    ax.set_ylabel("N", fontdict = fontmyxy)
    titulo=str(input("Histogram title: "))
    ax.set_title(titulo, fontdict = fontmytitle)
    plt.show
    # avline = plt.axvline(last_column.mean)


def fit_spectra(dictflargs):
    """
    Matplotlib inside the function ploting of a gaussian normalized curve.

    Inputs
    ----------
    x : list
        x axis values list or array, returned by default from the specific method plotting function (ex: draw_graph)

    y : list
        y axis values list or array, returned by default from the specific method plotting function (ex: draw_graph)

    dictflargs  :  Dictionary
        Dictionary containing all the user input values, or default values in case the user don't input, used in this function to obtain the curve baseline

    w1 : float
        Inferior x axis value that defines the range of normalization

    w2 : float
        Superior x axis value that defines the range of normalization

    titulo_norm : string
        Title of the normalized graphic, extracted from the untreated plotting function

    nciclos : integer
        given by the specific method plotting function (ex: draw_graph), count the amount of plotted functions

    Returns
    -------


    Exemplo
    -------
    >>> eixo_ynorm = fit_spectra(eixo_x, eixo_y, 400, 1200, 1300)
    eixo_ynorm: [array normalizada]

    Customização
    ------------
    stddev : float
        Desvio padrão da curva normalizada

    """
    file = file_path()
    eixo_x, eixo_y = axis_xy_fl(file)
    maxpos = eixo_y.argmax()
    maxpos = maxpos + eixo_x[0]
    w1 = dictflargs["w1"]
    w2 = dictflargs["w2"]
    if dictflargs["gaussian_norm"]:
        baseline = dictflargs["baseline"]
    else:
        baseline = eixo_y.min()
    amp = eixo_y.max() - baseline
    spectrum = Spectrum1D(flux = eixo_y * (u.ct / u.s), spectral_axis = eixo_x * u.nm)
    g_init = models.Gaussian1D(amplitude = amp * (u.ct / u.s), mean = maxpos * u.nm, stddev = 0.2 * u.nm)
    g_fit = fit_lines(spectrum, g_init, window = (w1 * u.nm, w2 * u.nm))
    y_fit = g_fit(eixo_x * u.nm)
    fig, ax = plt.subplots()
    ax.plot(eixo_x, y_fit, color = palettes[nciclos])
    ax.set_title(titulo_norm, fontdict = fontmytitle)
    ax.set_xlabel("Wavelength (nm)", )
    ax.set_ylabel("CPS")
    ax.grid()


# |%%--%%| <7IXmuLSbgz|xY2SgZbt3A>
r"""°°°
<br>

### main.py
°°°"""
# |%%--%%| <xY2SgZbt3A|ZRcgtttyRS>

# -*- coding: ISO-8859-1 -*-
"""
Created on Tue Mar 21 20:45:25 2023

@author: eduardo
"""
import functions_apply as fa
import matplotlib

matplotlib.use("Qt5Cairo")


def _main():
    fa.plot_functions()


if __name__ == "__main__":
    _main()

# TODO: Configure normalization of the different plots
#  Configure fonts of matplotlib
#  Configure size distribution histogram curve plot
#  Fix functions axis_xy_gc, making it separate hte important part of the csv by index and slice
#  Make a function that isolate and calculate the areas of the peaks in hte gc csv
#  Correct label of  multiple plots, they are getting all the title
#  Implement isnumeric in my axis_xy functions, automatizing the detection of when the useful data in a ASCII file starts, maybe merge fl and gc functions
#  Check the necessity of the file of distinctipy, or if is better to justo used the installed pip module
#  Possibly substitute nciclos in all functions to a argument passed in dictflargs (optionally?)


# TODO Detailed tests already ran to check if the main function is WORKING
#  Fluorescence emission, 1 plot, generated color palette by input of pastel and ncolors
#  Fluorescence emission, 3 plot, generated color palette by input of pastel and ncolors
#  Fluorescence emission, 1 plot, using pre-defined color argument (--color pink2)
#  Fluorescence emission, 1 plot, using pre-defined color palette as argument (--custom-palette my_palette_rgb)
#  Fluorescence emission, 3 plot, using pre-defined color palette as argument (--custom-palette my_palette_rgb)
#  Gas Chromatography, 1 plot, no color drguments
#  Histogram bar of tem csv plotting, without mean line, defining color by the name (--color), using default fonts for axis and title, and interactively
#  defining the
#  plot title
#  Histogram bar of tem csv, inputting axis font, generating the plot color with pastel and ncolors (it was grey)


# TODO New installation module notebook, python 3.10, anaconda3 enviroment, main envelope, bb

# |%%--%%| <ZRcgtttyRS|2a5GTf3mAQ>
r"""°°°
<br>

### init.py
°°°"""
# |%%--%%| <2a5GTf3mAQ|JXKbaiSY3c>
r"""°°°
<br>

### Functions apply
°°°"""
# |%%--%%| <JXKbaiSY3c|CF4i2EBpBO>

# -*- coding: ISO-8859-1 -*-
import matplotlib.pyplot as plt
import program_functions as pf
import functions as ft
from specutils import Spectrum1D

def plot_functions():
    dictflargs = pf.ft_commands()  # Function that store the values of an interactive input of the user, based on pre-defined possibilities
    palettes = pf.color_utils(dictflargs)
    if dictflargs["plot_flu"]:
        plot_typei = "fl"
        eixo_x, eixo_y, titulo_norm, arquivo, nciclos = ft.draw_graph(palettes, plot_typei, dictflargs)
    elif dictflargs["plot_gc"]:
        plot_typei = "gc"
        eixo_x, eixo_y, titulo_norm, arquivo, nciclos = ft.draw_graph(palettes, plot_typei, dictflargs)
    elif dictflargs["size_distribution"]:
        plot_typei = "tem"
        ft.plot_distribution(dictflargs, palettes)
    elif dictflargs["gaussian_norm"]:
        ft.fit_spectra(dictflargs)
    elif dictflargs["helpmy"]:
        pf.show_help()
    graphs = plt.show()
    return graphs

# |%%--%%| <CF4i2EBpBO|mS6BvUanGq>
r"""°°°
<br>


## Distinctipy
---
°°°"""
# |%%--%%| <mS6BvUanGq|kL2ZxCX0Gj>

#!/usr/bin/nv python
# -*- coding: utf-8 -*-

"""
[eduardotcampos@usp.br
[07/15/23 : 6:25 AM]
"""

import math
import random
import numpy as np
fBlind = {
    "Normal": lambda v: v,
    "Protanopia": lambda v: blindMK(v, "protan"),
    "Protanomaly": lambda v: anomylize(v, blindMK(v, "protan")),
    "Deuteranopia": lambda v: blindMK(v, "deutan"),
    "Deuteranomaly": lambda v: anomylize(v, blindMK(v, "deutan")),
    "Tritanopia": lambda v: blindMK(v, "tritan"),
    "Tritanomaly": lambda v: anomylize(v, blindMK(v, "tritan")),
    "Achromatopsia": lambda v: monochrome(v),
    "Achromatomaly": lambda v: anomylize(v, monochrome(v)),
}

# pre-define interesting colours/points at corners, edges, faces and interior of
# r,g,b cube
WHITE = (1.0, 1.0, 1.0)
BLACK = (0.0, 0.0, 0.0)
RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)
CYAN = (0.0, 1.0, 1.0)
YELLOW = (1.0, 1.0, 0.0)
MAGENTA = (1.0, 0.0, 1.0)

CORNERS = [WHITE, BLACK, RED, GREEN, BLUE, CYAN, YELLOW, MAGENTA]

MID_FACE = [
    (0.0, 0.5, 0.0),
    (0.0, 0.0, 0.5),
    (0.0, 1.0, 0.5),
    (0.0, 0.5, 1.0),
    (0.0, 0.5, 0.5),
    (0.5, 0.0, 0.0),
    (0.5, 0.5, 0.0),
    (0.5, 1.0, 0.0),
    (0.5, 0.0, 0.5),
    (0.5, 0.0, 1.0),
    (0.5, 1.0, 0.5),
    (0.5, 1.0, 1.0),
    (0.5, 0.5, 1.0),
    (1.0, 0.5, 0.0),
    (1.0, 0.0, 0.5),
    (1.0, 0.5, 0.5),
    (1.0, 1.0, 0.5),
    (1.0, 0.5, 1.0),
]

INTERIOR = [
    (0.5, 0.5, 0.5),
    (0.75, 0.5, 0.5),
    (0.25, 0.5, 0.5),
    (0.5, 0.75, 0.5),
    (0.5, 0.25, 0.5),
    (0.5, 0.5, 0.75),
    (0.5, 0.5, 0.25),
]

POINTS_OF_INTEREST = CORNERS + MID_FACE + INTERIOR


_SEED_MAX = int(2**32 - 1)


def _ensure_rng(rng):
    """
    Returns a random.Random state based on the input
    """
    if rng is None:
        rng = random._inst
    elif isinstance(rng, int):
        rng = random.Random(int(rng) % _SEED_MAX)
    elif isinstance(rng, float):
        rng = float(rng)
        # Coerce the float into an integer
        a, b = rng.as_integer_ratio()
        if b == 1:
            seed = a
        else:
            s = max(a.bit_length(), b.bit_length())
            seed = (b << s) | a
        rng = random.Random(seed % _SEED_MAX)
    elif isinstance(rng, random.Random):
        rng = rng
    else:
        raise TypeError(type(rng))
    return rng


def get_random_color(pastel_factor=0, rng=None):
    """
    Generate a random rgb colour.

    :param pastel_factor: float between 0 and 1. If pastel_factor>0 paler colours will
        be generated.

    :param rng: A random integer seed or random.Random state.
        If unspecified the global random is used.

    :return: color: a (r,g,b) tuple. r, g and b are values between 0 and 1.
    """
    rng = _ensure_rng(rng)

    color = [(rng.random() + pastel_factor) / (1.0 + pastel_factor) for _ in range(3)]

    return tuple(color)


def color_distance(c1, c2):
    """
    Metric to define the visual distinction between two (r,g,b) colours.
    Inspired by: https://www.compuphase.com/cmetric.htm

    :param c1: (r,g,b) colour tuples. r,g and b are values between 0 and 1.

    :param c2: (r,g,b) colour tuples. r,g and b are values between 0 and 1.

    :return: distance: float representing visual distinction between c1 and c2.
        Larger values = more distinct.
    """

    r1, g1, b1 = c1
    r2, g2, b2 = c2

    mean_r = (r1 + r2) / 2
    delta_r = (r1 - r2) ** 2
    delta_g = (g1 - g2) ** 2
    delta_b = (b1 - b2) ** 2

    distance = (2 + mean_r) * delta_r + 4 * delta_g + (3 - mean_r) * delta_b

    return distance


def distinct_color(
    exclude_colors, pastel_factor=0, n_attempts=1000, colorblind_type=None, rng=None
):
    """
    Generate a colour as distinct as possible from the colours defined in exclude_colors
    Inspired by: https://gist.github.com/adewes/5884820

    :param exclude_colors: a list of (r,g,b) tuples. r,g,b are values between 0 and 1.

    :param pastel_factor: float between 0 and 1. If pastel_factor>0 paler colours will
        be generated.

    :param n_attempts: number of random colours to generate to find most distinct colour

    :param colorblind_type: Type of colourblindness to simulate, can be:

        * 'Normal': Normal vision
        * 'Protanopia': Red-green colorblindness (1% males)
        * 'Protanomaly': Red-green colorblindness (1% males, 0.01% females)
        * 'Deuteranopia': Red-green colorblindness (1% males)
        * 'Deuteranomaly': Red-green colorblindness (most common type: 6% males,
          0.4% females)
        * 'Tritanopia': Blue-yellow colourblindness (<1% males and females)
        * 'Tritanomaly' Blue-yellow colourblindness (0.01% males and females)
        * 'Achromatopsia': Total colourblindness
        * 'Achromatomaly': Total colourblindness

    :param rng: A random integer seed or random.Random state.
        If unspecified the global random is used.

    :return: (r,g,b) color tuple of the generated colour with the largest minimum
        color_distance to the colours in exclude_colors.
    """
    rng = _ensure_rng(rng)

    if not exclude_colors:
        return get_random_color(pastel_factor=pastel_factor, rng=rng)

    if colorblind_type:
        exclude_colors = [
            colorblind.colorblind_filter(color, colorblind_type)
            for color in exclude_colors
        ]

    max_distance = None
    best_color = None

    # try pre-defined corners, edges, interior points first
    if pastel_factor == 0:
        for color in POINTS_OF_INTEREST:
            if color not in exclude_colors:
                if colorblind_type:
                    compare_color = colorblind.colorblind_filter(color, colorblind_type)
                else:
                    compare_color = color

                distance_to_nearest = min(
                    [color_distance(compare_color, c) for c in exclude_colors]
                )

                if (not max_distance) or (distance_to_nearest > max_distance):
                    max_distance = distance_to_nearest
                    best_color = color

    # try n_attempts randomly generated colours
    for _ in range(n_attempts):
        color = get_random_color(pastel_factor=pastel_factor, rng=rng)

        if not exclude_colors:
            return color

        else:
            if colorblind_type:
                compare_color = colorblind_filter(color, colorblind_type)
            else:
                compare_color = color

            distance_to_nearest = min(
                [color_distance(compare_color, c) for c in exclude_colors]
            )

            if (not max_distance) or (distance_to_nearest > max_distance):
                max_distance = distance_to_nearest
                best_color = color

    return tuple(best_color)


def get_text_color(background_color, threshold=0.6):
    """
    Choose whether black or white text will work better on top of background_color.
    Inspired by: https://stackoverflow.com/a/3943023

    :param background_color: The colour the text will be displayed on

    :param threshold: float between 0 and 1. With threshold close to 1 white text will
        be chosen more often.

    :return: (0,0,0) if black text should be used or (1,1,1) if white text should be
        used.
    """

    r, g, b = background_color[0], background_color[1], background_color[2]

    if (r * 0.299 + g * 0.587 + b * 0.114) > threshold:
        return BLACK
    else:
        return WHITE


def get_colors(
    n_colors,
    exclude_colors=None,
    return_excluded=False,
    pastel_factor=0,
    n_attempts=1000,
    colorblind_type=None,
    rng=None,
):
    """
    Generate a list of n visually distinct colours.

    :param n_colors: How many colours to generate

    :param exclude_colors: A list of (r,g,b) colours that new colours should be distinct
        from. If exclude_colours=None then exclude_colours will be set to avoid white
        and black (exclude_colours=[(0,0,0), (1,1,1)]). (r,g,b) values should be floats
        between 0 and 1.

    :param return_excluded: If return_excluded=True then exclude_colors will be included
        in the returned color list. Otherwise only the newly generated colors are
        returned (default).

    :param pastel_factor: float between 0 and 1. If pastel_factor>0 paler colours will
        be generated.

    :param n_attempts: number of random colours to generated to find most distinct
        colour.

    :param colorblind_type: Generate colours that are distinct with given type of
        colourblindness. Can be:

            * 'Normal': Normal vision
            * 'Protanopia': Red-green colorblindness (1% males)
            * 'Protanomaly': Red-green colorblindness (1% males, 0.01% females)
            * 'Deuteranopia': Red-green colorblindness (1% males)
            * 'Deuteranomaly': Red-green colorblindness (most common type: 6% males,
            0.4% females)
            * 'Tritanopia': Blue-yellow colourblindness (<1% males and females)
            * 'Tritanomaly' Blue-yellow colourblindness (0.01% males and females)
            * 'Achromatopsia': Total colourblindness
            * 'Achromatomaly': Total colourblindness

    :param rng: A random integer seed or random.Random state.
        If unspecified the global random is used.

    :return: colors - A list of (r,g,b) colors that are visually distinct to each other
        and to the colours in exclude_colors. (r,g,b) values are floats between 0 and 1.
    """
    rng = _ensure_rng(rng)

    if exclude_colors is None:
        exclude_colors = [WHITE, BLACK]

    colors = exclude_colors.copy()

    for i in range(n_colors):
        colors.append(
            distinct_color(
                colors,
                pastel_factor=pastel_factor,
                n_attempts=n_attempts,
                colorblind_type=colorblind_type,
                rng=rng,
            )
        )

    if return_excluded:
        return colors
    else:
        return colors[len(exclude_colors) :]


def invert_colors(colors):
    """
    Generates inverted colours for each colour in the given colour list, using a simple
    inversion of each colour to the opposite corner on the r,g,b cube.

    :return: inverted_colors - A list of inverted (r,g,b) (r,g,b) values are floats
        between 0 and 1.
    """
    inverted_colors = []

    for color in colors:
        r = 0.0 if color[0] > 0.5 else 1.0
        g = 0.0 if color[1] > 0.5 else 1.0
        b = 0.0 if color[2] > 0.5 else 1.0

        inverted_colors.append((r, g, b))

    return inverted_colors


def color_swatch(
    colors,
    edgecolors=None,
    show_text=False,
    text_threshold=0.6,
    ax=None,
    title=None,
    one_row=None,
):
    """
    Display the colours defined in a list of colors.

    :param colors: List of (r,g,b) colour tuples to display. (r,g,b) should be floats
        between 0 and 1.

    :param edgecolors: If None displayed colours have no outline. Otherwise a list of
        (r,g,b) colours to use as outlines for each colour.

    :param show_text: If True writes the background colour's hex on top of it in black
        or white, as appropriate.

    :param text_threshold: float between 0 and 1. With threshold close to 1 white text
        will be chosen more often.

    :param ax: Matplotlib axis to plot to. If ax is None plt.show() is run in function
        call.

    :param title: Add a title to the colour swatch.

    :param one_row: If True display colours on one row, if False as a grid. If
        one_row=None a grid is used when there are more than 8 colours.

    :return:
    """
    import matplotlib.colors
    import matplotlib.patches as patches
    import matplotlib.pyplot as plt

    if one_row is None:
        if len(colors) > 8:
            one_row = False
        else:
            one_row = True

    if one_row:
        n_grid = len(colors)
    else:
        n_grid = math.ceil(np.sqrt(len(colors)))

    width = 1
    height = 1

    x = 0
    y = 0

    max_x = 0
    max_y = 0

    if ax is None:
        show = True
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, aspect="equal")
    else:
        show = False

    for idx, color in enumerate(colors):
        if edgecolors is None:
            ax.add_patch(patches.Rectangle((x, y), width, height, color=color))
        else:
            ax.add_patch(
                patches.Rectangle(
                    (x, y),
                    width,
                    height,
                    facecolor=color,
                    edgecolor=edgecolors[idx],
                    linewidth=5,
                )
            )

        if show_text:
            ax.text(
                x + (width / 2),
                y + (height / 2),
                matplotlib.colors.rgb2hex(color),
                fontsize=60 / np.sqrt(len(colors)),
                ha="center",
                color=get_text_color(color, threshold=text_threshold),
            )

        if (idx + 1) % n_grid == 0:
            if edgecolors is None:
                y += height
                x = 0
            else:
                y += height + (height / 10)
                x = 0
        else:
            if edgecolors is None:
                x += width
            else:
                x += width + (width / 10)

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    ax.set_ylim([-height / 10, max_y + 1.1 * height])
    ax.set_xlim([-width / 10, max_x + 1.1 * width])
    ax.invert_yaxis()
    ax.axis("off")

    if title is not None:
        ax.set_title(title)

    if show:
        plt.show()


def get_hex(color):
    """
    Returns hex of given color

    :param color: (r,g,b) color tuple. r,g,b are floats between 0 and 1.

    :return: hex str of color
    """
    import matplotlib.colors

    return matplotlib.colors.rgb2hex(color)


def get_rgb256(color):
    """
    Converts 0.0-1.0 rgb colour into 0-255 integer rgb colour.

    :param color: (r,g,b) tuple with r,g,b floats between 0.0 and 1.0

    :return: (r,g,b) ints between 0 and 255
    """
    return (
        int(round(color[0] * 255)),
        int(round(color[1] * 255)),
        int(round(color[2] * 255)),
    )


def get_colormap(list_of_colors, name="distinctipy"):
    """
    Converts a list of colors into a matplotlib colormap.

    :param list_of_colors: a list of (r,g,b) color tuples. (r,g,b) values should be
        floats between 0 and 1.

    :param name: name of the generated colormap

    :return: cmap: a matplotlib colormap.
    """
    import matplotlib.colors

    cmap = matplotlib.colors.ListedColormap(list_of_colors, name=name)

    return cmap

def colorblind_filter(color, colorblind_type="Deuteranomaly"):
    """
    Transforms an (r,g,b) colour into a simulation of how a person with colourblindnes
    would see that colour.

    :param color: rgb colour tuple to convert

    :param colorblind_type: Type of colourblindness to simulate, can be:

        * 'Normal': Normal vision
        * 'Protanopia': Red-green colorblindness (1% males)
        * 'Protanomaly': Red-green colorblindness (1% males, 0.01% females)
        * 'Deuteranopia': Red-green colorblindness (1% males)
        * 'Deuteranomaly': Red-green colorblindness (most common type: 6% males,
          0.4% females)
        * 'Tritanopia': Blue-yellow colourblindness (<1% males and females)
        * 'Tritanomaly' Blue-yellow colourblindness (0.01% males and females)
        * 'Achromatopsia': Total colourblindness
        * 'Achromatomaly': Total colourblindness

    :return:
    """
    filter_function = fBlind[colorblind_type]

    return filter_function(color)

