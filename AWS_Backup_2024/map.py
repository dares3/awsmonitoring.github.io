import plotly.express as px
import matplotlib.colors as clrs
import numpy as np
from plotly.offline import plot
import pandas as pd
from datetime import datetime, timedelta
import shutil, os


lat = [
-6.868166 ,
1.165106 ,
-0.916019,
-2.919324,
-3.643831,
3.2162,
5.313331 ,
5.81392 ,
4.049,
1.553099 ,
-0.349350,
-4.781,
-2.7502,
-1.0423,
0.6385,
1.1211,
-1.4203,
3.327173 ,
-8.4883,
0.8292,
-1.8725,
-6.0988,
-5.8511,
-5.7542,
-7.9824,
-8.6354,
-9.6693,
-10.7663,
3.9119,
-2.0702,
-3.8867,
-3.8583,
-1.5105561
]

lat = np.array(lat)

lon = [
109.1209608,
97.704584,
119.90518,
132.264938,
133.696869,
106.2183,
95.12961,
96.34616,
96.2478,
98.897437,
102.334084,
104.5767,
107.7502,
122.7709,
122.8524,
120.7943,
120.6569,
117.570436,
117.4133,
127.3816,
138.7519,
140.3011,
112.6579,
132.7577,
131.2982,
122.2377,
120.2997,
123.0736,
108.3934,
125.9789,
130.8954,
102.3364,
134.1772874
]

lon = np.array(lon)

data = np.array(["OFF"]*33)

text = [
"Tegal",
"Gunung Sitoli",
"Palu",
"Fak-Fak",
"Kaimana",
"Tarempa",
"Cut Bau Sabang",
"Malikussaleh",
"Meulaboh",
"Sibolga",
"Japura Rengat",
"Dabo Singkep",
"Tanjung Pandan",
"Luwuk",
"Gorontalo",
"Toli-Toli",
"Poso",
"Tarakan",
"Sumbawa",
"Ternate",
"Sarmi",
"Tanah Merah",
"Bawean",
"Tual",
"Saumlaki",
"Maumere",
"Waingapu",
"Rote",
"Ranai",
"Sanana",
"Geser",
"Bengkulu",
"Manokwari"
]


size = np.ones(33)*5

center = {
'lat': -2.600029, 
'lon': 118.015776
}


dataset = {
'lat': lat,
'lon': lon,
'status':data
}

df = pd.DataFrame(dataset)

print(df)

fig = px.scatter_mapbox(df, lat="lat", lon="lon", center = center, size = size, size_max = 10, text = text,
						color='status', zoom=3.5, title = 'TBR AWS CENTER',
						mapbox_style='open-street-map')
#'''
plot(fig, auto_open=True)

#shutil.copyfile('temp-plot.html','/var/www/html/temp-plot.html')
shutil.copyfile('temp-plot.html','/home/tbr-obs/dares3.github.io/temp-plot.html')
os.system("cd /home/tbr-obs/dares3.github.io/")
os.system("git add .")
os.system("git commit -am 'updated'")
os.system("git push")
