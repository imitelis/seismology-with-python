from pandas.io.formats import style
import pygmt
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

minlon, maxlon = 85, 123
minlat, maxlat = 40, 53

grid = pygmt.datasets.load_earth_relief(resolution="05m", region=[minlon, maxlon, minlat, maxlat])
fig = pygmt.Figure()
erqdata = pd.read_csv('/home/cogito/Desktop/RegionearthquakeUSGS.csv')
pygmt.makecpt(cmap="magma", series=[erqdata.depth.min(), erqdata.depth.max()])

fig.basemap(
    region=[minlon, maxlon, minlat, maxlat],
    projection="M4i",
    frame=["a", '+t"Mongolia; Earthquakes 1900-2022, Geo Faults"'])

fig.coast(
    borders=["1/0.5p,black", "2/0.5p,red", "3/0.5p,blue"],
    land="dimgray",
    water="gray")

fig.plot(
    x=[110.46, 108.44],
    y=[44.46, 43.28],
    pen="0.5p,red")

fig.plot(
    x=[114.39, 113.47],
    y=[45.37, 45.21],
    pen="0.5p,red")

fig.plot(
    x=[116.14, 117.59],
    y=[47.07, 47.19],
    pen="0.5p,red")

fig.plot(
    x=[101.36, 98.44, 99.40],
    y=[45.35, 47.24, 47.21],
    pen="0.5p,red")

fig.plot(
    x=[115.16, 114.03, 112.03],
    y=[47.45, 46.58, 45.57],
    pen="0.5p,red")

fig.plot(
    x=[110.55, 109.37, 107.56],
    y=[44.23, 43.17, 42.42],
    pen="0.5p,red")

fig.plot(
    x=[116.53, 116.29, 115.51],
    y=[46.52, 46.30, 46.15],
    pen="0.5p,red")

fig.plot(
    x=[90.04, 91.46],
    y=[49.04, 47.17],
    pen="0.5p,red")

fig.plot(
    x=[116.05, 115.09, 114.17, 113.24],
    y=[46.49, 46.13, 45.47, 45.34],
    pen="0.5p,red")

fig.plot(
    x=[115.39, 114.55, 113.51, 113.03],
    y=[47.01, 46.24, 46.01, 45.42],
    pen="0.5p,red")

fig.plot(
    x=[110.11, 108.19, 107.06, 104.49, 104.00],
    y=[44.57, 44.32, 44.16, 44.16, 44.34],
    pen="0.5p,red")

fig.plot(
    x=[105.45, 105.09],
    y=[42.49, 43.04],
    pen="0.5p,red")

fig.plot(
    x=[99.07, 97.49],
    y=[46.20, 46.17],
    pen="0.5p,red")

fig.plot(
    x=[103.35, 102.02, 100.10],
    y=[43.48, 44.09, 44.39],
    pen="0.5p,red")

fig.plot(
    x=[103.55, 102.08],
    y=[49.50, 49.31],
    pen="0.5p,red")

fig.plot(
    x=[102.37, 100.08, 99.17],
    y=[42.40, 43.02, 43.03],
    pen="0.5p,red")

fig.plot(
    x=[101.35, 100.29],
    y=[43.37, 43.42],
    pen="0.5p,red")

fig.plot(
    x=[102.37, 103.18, 104.28],
    y=[43.31, 43.26, 42.41],
    pen="0.5p,red")

fig.plot(
    x=[102.54, 101.16, 99.34, 99.02, 95.58, 95.26],
    y=[43.32, 43.24, 43.22, 43.29, 43.28, 43.22],
    pen="0.5p,red")

fig.plot(
    x=[98.08, 97.27],
    y=[43.46, 43.48],
    pen="0.5p,red")

fig.plot(
    x=[97.09, 95.42],
    y=[43.57, 44.02],
    pen="0.5p,red")

fig.plot(
    x=[97.24, 95.54],
    y=[45.33, 45.30],
    pen="0.5p,red")

fig.plot(
    x=[97.24, 95.54],
    y=[45.33, 45.30],
    pen="0.5p,red")

fig.plot(
    x=[95.01, 95.00],
    y=[45.39, 45.53],
    pen="0.5p,red")

fig.plot(
    x=[92.37, 92.08],
    y=[45.32, 45.26],
    pen="0.5p,red")

fig.plot(
    x=[95.36, 95.26, 94.48],
    y=[46.35, 46.26, 46.22],
    pen="0.5p,red")

fig.plot(
    x=[98.09, 96.59],
    y=[49.32, 49.39],
    pen="0.5p,red")

fig.plot(
    x=[101.33, 100.38, 99.10],
    y=[49.50, 49.45, 49.17],
    pen="0.5p,red")

fig.plot(
    x=[99.21, 95.02, 92.53],
    y=[49.04, 49.18, 49.55],
    pen="0.5p,red")

fig.plot(
    x=[101.58, 101.17, 101.45],
    y=[50.28, 50.11, 49.52],
    pen="0.5p,red")

fig.plot(
    x=[101.17, 100.18],
    y=[50.11, 50.19],
    pen="0.5p,red")

fig.plot(
    x=[104.06, 103.09, 101.50],
    y=[45.49, 46.52, 48.41],
    pen="0.5p,red")

fig.plot(
    x=[102.02, 102.10],
    y=[47.52, 47.06],
    pen="0.5p,red")

fig.plot(
    x=[102.04, 101.09],
    y=[47.28, 47.29],
    pen="0.5p,red")

fig.plot(
    x=[101.18, 101.06, 100.33],
    y=[48.16, 47.29, 47.05],
    pen="0.5p,red")

fig.plot(
    x=[93.35, 97.21],
    y=[48.11, 45.21],
    pen="0.5p,red")

fig.plot(
    x=[101.26, 96.45],
    y=[44.31, 45.21],
    pen="0.5p,red")

fig.plot(
    x=[101.47, 100.20, 95.02],
    y=[43.47, 43.39, 45.21],
    pen="0.5p,red")

fig.plot(
    x=[97.21, 95.49, 93.47],
    y=[43.38, 43.59, 44.53],
    pen="0.5p,red")

fig.plot(
    x=[93.53, 93.45, 94.21],
    y=[46.43, 48.40, 49.11],
    pen="0.5p,red")

fig.plot(
    x=[93.53, 92.34, 92.38],
    y=[46.43, 48.36, 49.47],
    pen="0.5p,red")

fig.plot(
    x=[94.36, 93.48],
    y=[45.05, 44.55],
    pen="0.5p,red")

fig.plot(
    x=[91.56, 90.58],
    y=[46.41, 47.20],
    pen="0.5p,red")

fig.plot(
    x=[90.46, 91.15, 91.29, 92.34],
    y=[46.54, 46.12, 45.22, 44.13],
    pen="0.5p,red")

fig.plot(
    x=[91.20, 93.02, 94.24],
    y=[46.07, 45.54, 45.19],
    pen="0.5p,red")

fig.plot(
    x=[94.30, 94.17, 93.53],
    y=[45.43, 46.14, 46.32],
    pen="0.5p,red")

fig.plot(
    x=[94.21, 93.35, 92.53],
    y=[45.35, 46.36, 47.14],
    pen="0.5p,red")

fig.plot(
    x=[91.18, 91.47, 92.11],
    y=[49.03, 48.10, 47.53],
    pen="0.5p,red")

fig.plot(
    x=[93.36, 92.34, 91.57, 91.28, 91.25],
    y=[45.40, 46.44, 47.22, 48.05, 48.32],
    pen="0.5p,red")

fig.plot(
    x=[91.18, 90.57],
    y=[48.18, 48.34],
    pen="0.5p,red")

fig.plot(
    x=erqdata.longitude,
    y=erqdata.latitude,
    size=0.02 * (erqdata['mag']),
    style="cc",
    color=erqdata.depth,
    cmap = True,
    pen="black",
    transparency=40)

fig.colorbar(frame='af+l"Depth in Km"')

fig.show()