# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:19:56 2023
@author: CEERMA
"""
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Load data
station = ("data/drake_plastico.csv")
st = pd.read_csv(
    station,
    names = [
        "estacao",  "initial_latitude", "final_latitude",
        "initial_longitude", "final_longitude"
    ],
    header = 0
)

#### Polar Stereographic Projection
# setup stereographic basemap.
# lat_ts is latitude of true scale.
# lon_0,lat_0 is central point.
m = Basemap(width=15000000,height=10000000,
            resolution='l',projection='stere',\
            lat_ts=80,lat_0=-55,lon_0=-60.,
            llcrnrlon=-75,urcrnrlon=-55,llcrnrlat=-63,urcrnrlat=-52)

m.drawmeridians(np.arange(0,360,10),labels=[0,0,0,1], fontweight="bold")
m.drawparallels(np.arange(-90,-40,5), labels=[1,0,0,0], fontweight="bold")
m.drawcoastlines()
m.drawcountries()

#### ETOPO
m.etopo(scale=0.5, alpha=0.5)
m.shadedrelief()

# ## Punta Arenas Coordenadas: 53° 9′ 0" S, 70° 55′ 0" W
# # Map (long, lat) to (x, y) for plotting
x, y = m(-70.9, -53.1)
x1, y1 = m(-70.2, -53.2)
plt.plot(x, y, 'ok', markersize=10)
plt.text(x1, y1, ' Punta Arenas', fontsize=12, fontweight="bold")
plt.plot(x, y, 'bo') # plot x and y using blue circle markers

for _, row in st.iterrows():
    lon1, lat1 = m(row['initial_longitude'], row['initial_latitude'])
    lon2, lat2 = m(row['final_longitude'], row['final_latitude'])
    plt.plot([lon1, lon2], [lat1, lat2], "-", linewidth=4, color='red')


plt.title(
    "MEPHYSTO OP42 Drake - Microplásticos", fontsize=10, fontweight="bold"
)
plt.savefig('results/drake_plastico.png', dpi=300)
