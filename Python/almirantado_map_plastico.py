# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:50:43 2023
@author: CEERMA
PLOT Baía do Almirantado e Estreito de Bransfield
"""
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib as plt
import numpy as np
import pygmt

# Load data --------------------------------------------------------------------
station = ("data/almirantado_plastico.csv")
st = pd.read_csv(
    station,
    names = [
        "estacao",  "initial_latitude", "final_latitude",
        "initial_longitude", "final_longitude", "stage"
    ],
    header = 0
)

# Start figure -----------------------------------------------------------------
fig = pygmt.Figure()

fig.coast(
    # Set the x-range from 10E to 20E and the y-range to 35N to 45N
    region = "-58.75/-58.0/-62.40/-62.0",
    # Set projection to Mercator, and the figure size to 15 centimeters
    projection = "M15c",
    land = "lightgray",
    # Set the color of the water to white
    water = "#99CCFF",
    # Display the national borders and set the pen thickness to 0.5p
    borders = "1/0.5p",
    # Display the shorelines and set the pen thickness to 0.5p
    shorelines = "1/0.5p",
    # Set the frame to display annotations and gridlines
    frame = "ag",
)
fig.basemap(frame = ["a", "+tMEPHYSTO OP42 - Microplásticos B. Almirantado"])
red_done = "no"
blue_done = "no"

for _, row in st.iterrows():
    if row['stage'] == 'ida':
        line_color = 'red'
        label = "1ª rodada"
        if red_done != "yes":
            fig.plot(
                x=[row["initial_longitude"], row["final_longitude"]],
                y=[row["initial_latitude"], row["final_latitude"]],
            frame="a",
            pen=f"2p,{line_color}",
            label = label
            )
            red_done = "yes"
        else:
            fig.plot(
                x=[row["initial_longitude"], row["final_longitude"]],
                y=[row["initial_latitude"], row["final_latitude"]],
                frame="a",
                pen=f"2p,{line_color}"
            )
    elif row['stage'] == 'volta':
        line_color = 'blue'
        label = "2ª rodada"
        if blue_done != "yes":
            fig.plot(
                x=[row["initial_longitude"], row["final_longitude"]],
                y=[row["initial_latitude"], row["final_latitude"]],
            frame="a",
            pen=f"2p,{line_color}",
            label = label
            )
            blue_done = "yes"
        else:
            fig.plot(
                x=[row["initial_longitude"], row["final_longitude"]],
                y=[row["initial_latitude"], row["final_latitude"]],
                frame="a",
                pen=f"2p,{line_color}"
            )
    elif row['stage'] == 'test':
        line_color = 'gold'
    else:
        line_color = 'black'  # or any default color

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
fig.plot(
    x = -58.39, y = -62.09, style = "c0.2c", fill = "black", pen = "black"
)
fig.text(
    text = "EACF", x = -58.36, y = -62.09, font = "10p,Helvetica-Bold,black"
)
fig.legend(position = "JTR+jTR", box = True)
fig.savefig('results/almirantado_plastico.png', dpi = 300)
print("image generated")
