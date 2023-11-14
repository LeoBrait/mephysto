# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:50:43 2023
@author: CEERMA
PLOT Baía do Almirantado e Estreito de Bransfield
"""
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pygmt

# Positions
station = ("data/almirantado_filtragens.csv")
st = pd.read_csv(station, names = ["station","latitude", "longitude"], header=0)
lat_ida = st['latitude'].values[0:6]
long_ida = st['longitude'].values[0:6]
lat_volta = st['latitude'].values[6:12]
long_volta = st['longitude'].values[6:12]
lat_nict = st['latitude'].values[12]
long_nict = st['longitude'].values[12]
print(st[0:6])
print(st[6:12])


fig = pygmt.Figure()
fig.coast(
    # Set the x-range from 10E to 20E and the y-range to 35N to 45N
    region="-58.75/-58.0/-62.40/-62.0",
    # Set projection to Mercator, and the figure size to 15 centimeters
    projection="M15c",
    # Set the color of the land to light gray
    land="lightgray",
    # Set the color of the water to white
    water="#99CCFF",
    # Display the national borders and set the pen thickness to 0.5p
    borders="1/0.5p",
    # Display the shorelines and set the pen thickness to 0.5p
    shorelines="1/0.5p",
    # Set the frame to display annotations and gridlines
    frame="ag",
)
fig.basemap(frame = ["a", "+tMEPHYSTO OP42 - Filtragens B. Almirantado"])

fig.plot(
    x = long_ida, y = lat_ida, style = "c0.3c", fill = "red", pen = "black",
    label="1ª rodada"
)
fig.plot(
    x = long_volta, y = lat_volta, style = "c0.3c", fill = "blue", pen = "black",
    label = "2ª rodada"
)
fig.plot(
    x = long_nict, y = lat_nict, style = "c0.3c", fill = "gold", pen = "black",
    label = "Nictemeral"
)

### Plot text annotations using single arguments
fig.text(
    text = "Estreito de Bransfield",
    x = -58.4, y = -62.35,
    font = "20p,Helvetica-Bold,black"
)
fig.text(
    text = "B. Almirantado",
    x = -58.58, y = -62.14,
    font = "18p,Helvetica-Bold,black"
)
fig.plot(x = -58.39, y = -62.09, style = "c0.2c", fill = "black", pen = "black")
fig.text(text = "EACF", x = -58.36, y = -62.09, font = "10p,Helvetica-Bold,black")
fig.legend(position = "JTR+jTR", box = True)

fig.savefig('results/almirantado_filtragens.png', dpi = 300)
