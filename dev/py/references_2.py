def closest(lst, K):
    """

    Finds the closest value in a list from a given number.

    Parameters
    ----------
    lst : list

    K : float

    Returns
    -------

    """
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]



    # plt.rcParams.update(
        # {
            # "savefig.directory": "/Programação/jupyter/IqDu/Attachments",
            # "savefig.format": "png",
            # "savefig.transparent": True,
        # }
    # )
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

def file_path():
    """
    Definir o path de um arquivo interativamente, pelo tkinter

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

# Old mpl png plotting, before transformed it to use pandas dataframe
import sys
sys.path.insert(1, '/home/eduardotc/Programação/my_gits/materials_chempy')
import utils as mc

def msplot(mzmlpath="/home/eduardotc/Programação/my_gits/materials_chempy/example_data/anad2.mzML", n_highest=20, n_labels=8, subtitle='default', manual_peak=False, manual_peak_mz=236, manual_peak_label='default', label1='Ion Trap ESI-MS', label2='Direct injection' ):
    """

    Plot a .mzML file in matplotlib.

    Plot a .mzML file in matplotlib, as a mz traces plot, of the user defined
    (or predefined) n highest mz peaks, with the possibility of adding general
    annotated labels to the plot, to define the number of mz peaks labeled with
    their value, minimal mz difference between two peaks to have both of the
    plotted and custom manual labeling of single mz peaks (to write to wich
    molecule it belongs for example).

    Parameters
    ----------
    mzmlpath : String
        String of the path to the .mzML file.

    n_highest : Integer
        Number of total mz peaks to be drawn, based on the highest intensities.

    n_labels : Integer
        Number of most intese peaks to be labeled with their m/z value.

    manual_peak : Boolean
        Define the manual labeling, with custom label, of one m/z peak.

    subtitle : String
        Plot subtitle, if not defined will be the parsed .mzML file name.

    manual_peak_mz : Float
        The m/z value of the desired manual annotated peak.

    manual_peak_label : String
        The manual annotation of the peak, for example, the molecule to which
        it belongs.

    label1 : String
        First label that appears in a box in the top right of the plot, for
        example, the mass spectrometry technique used.

    label2 : String
        Second label that appears in a box in the top right of the plot, for
        example, the injection method (like direct injection or hplc).

    Returns
    -------
    None
        Don't have return, but plot the spectrum and save it to a png.

    """
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import pyopenms
    import os

    # mc.matplotlib_config()    # Configuring the matplotlib tho utils defined style

    # Getting the name of the .mzML parsed file
    fname = os.path.basename(mzmlpath)
    fname = os.path.splitext(mzmlpath)[0]

    resolution_thrs=0.3

    # Load the spectra from the mzML file
    exp = pyopenms.MSExperiment()
    pyopenms.MzMLFile().load(mzmlpath, exp)

    # Extract the mass-to-charge ratios (m/z) and intensity values
    df = pd.DataFrame({'mz': [],
                       'intensity': []})
    for spectrum in exp:
        mz_array = spectrum.get_peaks()[0]
        intensity_array = spectrum.get_peaks()[1]
        mz_values.extend(mz_array)
        intensity_values.extend(intensity_array)

    mz_max = max(mz_values)    # Getting m/z max value
    int_max = max(intensity_values)    # Getting intensity max value
    ymax = int_max*1.2
    ylimit = [0, ymax]  # Defining the y axis limit of the plot

    # Calculate the baseline (simple mean in this example)
    baseline = np.mean(intensity_values)

    # Subtract the baseline from the intensity values
    intensity_values = np.array(intensity_values) - baseline


    # Initiate conditional variable counters
    total_indices = []
    total_indices.append(0)
    ncycle = 1
    diffms = True
    npeaks=0

    # Define the size and dpi of the image
    (
        fig,
        ax,
    ) = plt.subplots(figsize=(10, 6), dpi=200)

    # Defining the plot design
    ax.set_ylim(ylimit)
    ax.set_xlabel("m/z")
    ax.set_ylabel("Intensity")
    if subtitle == 'default':
        subtitle = fname
    fig.suptitle("f{subtitle}", fontsize=15, color='#3333b2')

    # Determine the number of highest intensity peaks to label (user-defined)
    ax.set_title("Mass spectrum")
    high_ind = np.array([])
    high_mz = np.array([])
    high_int = np.array([])

    # Conditional loop to plot the defined number of peaks
    while len(total_indices) <= n_highest:
        intaddind = np.argpartition(intensity_values, -ncycle)[-ncycle]
        mz = mz_values[intaddind]
        for i in total_indices:
            if abs(mz - i) < resolution_thrs:
                diffms = False
        if diffms:
            high_int = np.append(high_int, intensity_values[intaddind])
            high_mz = np.append(high_mz, mz_values[intaddind])

            # Conditional to automatic label the desired number of peaks
            if npeaks < n_labels:
                ax.annotate(
                    round(mz, 2), xy=(mz, intensity_values[intaddind]), fontsize=10
                )
                npeaks=npeaks+1
            total_indices.append(mz)
        ncycle = ncycle + 1
        diffms = True

    # Manual peak annotation
    if manual_peak:
        ax.annotate(
            (
                '$[M + 2H]^{+}$'
                '\n'
            ),
            xy=(236.74, 3.20e+6),
            fontsize=10,
            fontweight='bold',
        )

    # Defining a legend colored box
    axin2=ax.indicate_inset([(0.85*mz_max), (int_max), (0.2*mz_max), (0.18*int_max)], facecolor='#a6bcf8', edgecolor='#252a2d', alpha=0.35)

    # Defining the writtent content of the legend box
    ax.annotate(
        (
            f'{label1}'
            '\n'
            '\n'
            f'{label2}'
        ),
        xy=(0.9*mz_max, 1.03*int_max),
        fontsize=12,
        fontfamily='QTHelvet-black',
        fontweight='normal',
        color='#000000',
    )

    # Plotting the spectrum as line peaks
    ax.stem(high_mz, high_int, markerfmt="none")
    ax.plot
    plt.show

    # Saving the image


    plt.savefig(fname)
