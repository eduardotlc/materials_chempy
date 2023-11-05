r"""°°°
# Histogram csv plotting
---
---

- Based on a generated size distribution csv table by imagej, after measuring the nanoparticles electron transmission microscopy image

- generates a matplotlib histogram of the nanoparticles size distribution

- Plots in the histogram a normal curve based on your data, the closer your data is to a normal distribution, more the plotted curve will coincide with your histogram bins


## Defining the matplotlib parameters
---
°°°"""
# |%%--%%| <TPjfAC1MVj|CTZDQ7KhTT>

import matplotlib.pyplot as plt
from cycler import cycler
plt.rcParams["pdf.use14corefonts"] = True
# trigger core fonts for PS backend
plt.rcParams["ps.useafm"] = True
#plt.rcParams['backend'] = 'Agg'
plt.rcParams.update(
    {
        "figure.dpi": 100,
        "font.size": 18,
        "figure.facecolor": "white",
        "figure.figsize": [10, 6],
        "figure.frameon": True,
        "figure.titlesize": "large",
        "figure.titleweight": "bold",
        "figure.labelsize": "medium",
        "figure.labelweight": "normal",
        "figure.edgecolor": "#000000",
    }
)

plt.rcParams.update(
    {
        "font.style": "normal",
        "font.weight": "bold",
        "font.family": "QTHelvet-Black",
        "font.sans-serif": "QTHelvet-Black",
        "font.size": 18,
    }
)

plt.rcParams.update(
    {
        "axes.grid": True,
        "axes.grid.axis": "both",
        "axes.grid.which": "major",
        "axes.labelcolor": "#172038",
        "axes.edgecolor": "#bcbcbc",
        "axes.facecolor": "#eeeeee",
        "axes.linewidth": 1.0,
    }
)

plt.rcParams.update(
    {
        "grid.alpha": 1.0,
        "grid.color": "#b2b2b2",
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,
        "grid.alpha": 1.0,
    }
)

plt.rcParams.update(
    {
        "savefig.directory": "/Programação/jupyter/IqDu/Attachments",
        "savefig.format": "png",
        "savefig.transparent": True,
    }
)

plt.rcParams.update(
    {
        "xtick.color": "#bcbcbc",
        "xtick.labelsize": "medium",
        "xtick.major.pad": 3.5,
        "xtick.major.size": 3.5,
        "xtick.alignment": "center",
        "xtick.color": "#000000",
        "ytick.labelsize": "x-small",
        "ytick.major.pad": 3.5,
        "ytick.major.size": 3.5,
        "ytick.alignment": "center_baseline",
        "ytick.color": "#000000",
    }
)
plt.rcParams.update(
    {
        "axes.prop_cycle": cycler(
            "color",
            [
                "#7499ff",
                "#348ABD",
                "#988ED5",
                "#777777",
                "#FBC15E",
                "#8EBA42",
                "#FFB5B8",
            ],
        )
    }
)

# |%%--%%| <CTZDQ7KhTT|aXCyJGLwqm>
r"""°°°
<br>

## User defined variables
---

- ```myc``` defines how are your csv columns named, the default definition in this notebook is based on an imageJ particle size distribution table generation

- ```csv_path```is the path to your csv input file, the default is a example nanoparticle size distribution table, that is in the example_data folder

- ```ìmportant_column``` is the CSV column that contains the data of interest, to generate the histogram plot and the normal curve, defaulted here to the 'Length' 
°°°"""
# |%%--%%| <aXCyJGLwqm|jH1rc5ef8R>

import pandas as pd
csv_path='../example_data/pdag_imagej_sizedist.csv'
myc=['Area','Mean','Min','Max','Angle','Length']
important_column = 'Length'

# |%%--%%| <jH1rc5ef8R|OepdqqFq7a>
r"""°°°
## Analyzing your csv
---

If you don't know which columns your csv file contain, you can run the bellow cell after defining its path, to analyze the column names, and to see which column will be used in the plot
°°°"""
# |%%--%%| <OepdqqFq7a|sPLgiIzfrm>

df=pd.read_csv(csv_path)
df

# |%%--%%| <sPLgiIzfrm|P224QBJ4wX>

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm

# Reading the data and converting to a pandas dataframe
df=pd.read_csv(csv_path)
df=pd.DataFrame(df, columns=myc)

# Initializing the matplotlib plot
(
    fig,
    ax,
) = plt.subplots(figsize=(10, 6), dpi=200)

# Defining the title, subtitle, and axes title
ax.set_xlabel("Size (nm)")
ax.set_ylabel("Frequence")
fig.suptitle("Pd@Ag", fontsize=15, color='#3333b2')
ax.set_title("Size distribution")



# Plotting the histogram
plt.hist(df['Length'], bins=10, density=True)

# Getting and defining some plot values, used to generate the label box of the plot
ylim = ax.get_ylim()
xlim = ax.get_xlim()
infdrawx=xlim[1] - ((xlim[1] - xlim[0])*0.15)
infdrawy=ylim[1] - ((ylim[1] - ylim[0])*0.15)
extdrawx=((xlim[1] - xlim[0])*0.1)
extdrawy=((ylim[1] - ylim[0])*0.1)
anotx=infdrawx +((xlim[1] - xlim[0])*0.012)
anoty=infdrawy +((ylim[1] - ylim[0])*0.03)

# Creating the label box, upper right in the graph
axin2=ax.indicate_inset([infdrawx, infdrawy, extdrawx, extdrawy], facecolor='#a6bcf8', edgecolor='#252a2d', alpha=0.35)

# Creating the annotation that goes in the box
ax.annotate(
    (
        'HRTEM'
    ),
    xy=(anotx, anoty),
    fontsize=12,
    fontfamily='QTHelvet-black',
    fontweight='normal',
    color='#000000',
)

# Getting the data mean and standard deviation to use in the plotted normal curve
data_descript=df[important_column].describe()
mu=data_descript['mean']
std=data_descript['std']

x = np.linspace(11.1, 26.7)
y = norm.pdf(x, mu, std)
ax.plot(x, y, color='#86d9d3')
plt.show

# Uncomment last line to save the ploted figure

plt.savefig('pdaghist.png')

# |%%--%%| <P224QBJ4wX|EEPvBnl9zS>
r"""°°°
<br>

## Description Statistics LaTeX
---

To generate a description statistic table, formatted in LaTeX, based on the important_column variable defined before, run the bellow cell
°°°"""
# |%%--%%| <EEPvBnl9zS|EOmtrs1Kyu>

mytab=df[important_column].describe()
print(mytab.to_latex(index=True,

                  formatters={"name": str.upper},

                  float_format="{:.1f}".format,

)) 

# |%%--%%| <EOmtrs1Kyu|QSKfsGpPr0>


