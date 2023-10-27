# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:50:43 2023

@author: CEERMA

PLOT Baía do Almirantado e Estreito de Bransfield

INPUT: Arquivo "station_op42_csv.csv" com os valores de latitude e longitude
em graus e negativos.
"""

### loading the data

import pandas as pd

### Set path directory
cnv_path = input("Insert the directory: ")
# Extract the station position
station = (cnv_path + "station_op42_baia_csv.csv")
st = pd.read_csv(station, names = ["station","latitude", "longitude"], header=0)

## Station LEG
st_lat = st['latitude'].values[:]
st_lon = st['longitude'].values[:]
st_name = st['station'].values[:]

##########################################

import pygmt

###############################################################################
# Coordinates
# -----------
#
# A string of coordinates can be passed to ``region``, in the form of
# *xmin*/*xmax*/*ymin*/*ymax*.


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

fig.basemap(frame=["a", "+tAntártica"])
fig.plot(x=st_lon, y=st_lat, style="c0.3c", fill="red", pen="black")

### Plot text annotations using single arguments
fig.text(text="Estreito de Bransfield", x=-58.4, y=-62.28, font="20p,Helvetica-Bold,black")
fig.text(text="Ilha do Rei George", x=-58.25, y=-62.03, font="18p,Helvetica-Bold,black")
fig.plot(x=-58.39, y=-62.09, style="c0.2c", fill="black", pen="black")
fig.text(text="EACF", x=-58.36, y=-62.09, font="10p,Helvetica-Bold,black")

fig.savefig('MEPHYSTO OP41 LEG3.png', dpi=300)
fig.show()
