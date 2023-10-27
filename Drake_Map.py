# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:19:56 2023

@author: CEERMA

PLOT DA PASSAGEM DE DRAKE

INPUT: Arquivo "station_op42_csv.csv" com os valores de latitude e longitude
em graus e negativos.
"""
### loading the data

import pandas as pd

### Set path directory
cnv_path = input("Insert the directory: ")

# Extract the station position
## AJUSTAR PARA PEGAR AS POSIÇÕES E MONTAR ARQUIVO AUTOMÁTICO!!!
station = (cnv_path + "station_op42_csv.csv")
st = pd.read_csv(station, names = ["station","latitude","longitude"], header=0)

## Station
st_lat = st['latitude'].values[:]
st_lon = st['longitude'].values[:]
st_name = st['station'].values[:]

# import os
# os.environ["PROJ_LIB"] = "C:\\Utilities\\Python\\Anaconda\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


#### Polar Stereographic Projection
# setup stereographic basemap.
# lat_ts is latitude of true scale.
# lon_0,lat_0 is central point.
m = Basemap(width=15000000,height=10000000,
            resolution='l',projection='stere',\
            lat_ts=80,lat_0=-55,lon_0=-60.,
            llcrnrlon=-80,urcrnrlon=-50,llcrnrlat=-65,urcrnrlat=-50)

m.drawmeridians(np.arange(0,360,10),labels=[0,0,0,1], fontweight="bold")
m.drawparallels(np.arange(-90,-40,5), labels=[1,0,0,0], fontweight="bold")
m.drawcoastlines()
m.drawcountries()

#### ETOPO
m.etopo(scale=0.5, alpha=0.5)
# draw a shaded-relief image
m.shadedrelief()

##### Station position
plt.plot(st_lon, st_lat, "*", markersize=10, color="r")

xll, yll = m(-60.5,-60.77) # <-- find those points by looking at meridians and parallels
xur, yur = m(-59.2,-61.13)
x3, y3 = m(-57.35,-61.64)
x4, y4 = m(-62.06, -59.77)
x5, y5 = m(-62.28, -59.546)
x6, y6 = m(-62.44, -59.39)
x7, y7 = m(-62.64, -59.2)
x8, y8 = m(-62.87, -59.02)

m.scatter([xll,xur, x3, x4, x5, x6, x7, x8], [yll, yur, y3, y4, y5, y6, y7, y8], c="crimson")

###### Plot trajectories
# m.plot(lon1,lat1, "--", linewidth=1.5,color='k')

# ## Punta Arenas Coordenadas: 53° 9′ 0" S, 70° 55′ 0" W
# # Map (long, lat) to (x, y) for plotting
x, y = m(-70.9, -53.1)
x1, y1 = m(-69.0, -53.1)
plt.plot(x, y, 'ok', markersize=10)
plt.text(x1, y1, ' Punta Arenas', fontsize=12, fontweight="bold");
plt.plot(x, y, 'bo') # plot x and y using blue circle markers


plt.title("MEPHYSTO OP42 (2023) - Drake", fontsize=10, fontweight="bold")

plt.savefig('MEPHYSTO OP41 LEG2.png', dpi=300)

plt.show()
