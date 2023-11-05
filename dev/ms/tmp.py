mzmlpath="/home/eduardotc/Programação/my_gits/materials_chempy/example_data/anad2.mzML"
n_highest=20
n_labels=8
subtitle='default'
manual_peak=False
manual_peak_mz=236
manual_peak_label='default'
label1='Ion Trap ESI-MS'
label2='Direct injection'


#|%%--%%| <2vwyq7TW6I|3WSABgekcx>
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

#|%%--%%| <3WSABgekcx|Qjudp1iKgm>

for spectrum in exp:
    df = pd.DataFrame({'mz': spectrum.get_peaks()[0],
                   'intensity': spectrum.get_peaks()[1]})
mz_max = (df['mz'].max())
int_max = (df['intensity'].max())
ymax = 1.2*int_max
ylimit = [0,ymax]
baseline = df['intensity'].mean()
df['intensity'] = df['intensity'] - baseline
print(df)
ax,  e
df.plot()

