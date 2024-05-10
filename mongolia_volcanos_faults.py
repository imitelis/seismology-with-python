import pygmt
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

minlon, maxlon = 85, 123
minlat, maxlat = 40, 53

grid = pygmt.datasets.load_earth_relief(resolution="05m", region=[minlon, maxlon, minlat, maxlat])
fig = pygmt.Figure()

pygmt.makecpt(
    cmap='geo',
    series='-1000/4000/1000',
    continuous=True)

fig.basemap(
    region=[minlon, maxlon, minlat, maxlat],
    projection="M4i",
    frame=["a", '+t"Elevation, volcanoes (b = extinct, g = normal / dormant)"'])

fig.grdimage(
    grid=grid,
    region=[minlon, maxlon, minlat, maxlat],
    projection='M4i',
    shading=True,
    frame=True)

fig.grdcontour(
    grid=grid,
    interval=4000,
    annotation="4000+f6p",
    limit="-8000/0",
    pen="a0.15p")

fig.coast(
    region=[minlon, maxlon, minlat, maxlat],
    projection='M4i',
    borders=["1/0.5p,black", "2/0.5p,red", "3/0.5p,blue"],
    shorelines=True,
    frame=True)

fig.coast(
    water="blue", 
    transparency=75)

fig.colorbar(
    frame='+l"Elevation in Km"')

fig.plot(x=99.7, y=48, style="t0.2c", color="green", pen="black")
fig.plot(x=102.7, y=48.5, style="t0.2c", color="green", pen="black")
fig.plot(x=114, y=45.1, style="t0.2c", color="green", pen="black")
fig.plot(x=102.4, y=51.3, style="t0.2c", color="green", pen="black")
fig.plot(x=120.7, y=47.3, style="t0.2c", color="green", pen="black")
fig.plot(x=89.3, y=42.8, style="t0.2c", color="green", pen="black")
fig.plot(x=98.6, y=52.4, style="t0.2c", color="green", pen="black")
fig.plot(x=99, y=52.7, style="t0.2c" , color="green", pen="black")
fig.plot(x=113, y=41.2, style="t0.2c" , color="black", pen="black")
fig.plot(x=118.5, y=42, style="t0.2c" , color="black", pen="black")
fig.plot(x=115.5, y=43.7, style="t0.2c" , color="black", pen="black")
fig.plot(x=107.5, y=42.3, style="t0.2c" , color="black", pen="black")
fig.plot(x=106, y=42.1, style="t0.2c" , color="black", pen="black")
fig.plot(x=104, y=43.3, style="t0.2c" , color="black", pen="black")
fig.plot(x=102.1, y=42.7, style="t0.2c" , color="black", pen="black")
fig.plot(x=103.5, y=44.1, style="t0.2c" , color="black", pen="black")
fig.plot(x=102, y=44.3, style="t0.2c" , color="black", pen="black")
fig.plot(x=109.1, y=47, style="t0.2c" , color="black", pen="black")
fig.plot(x=107.7, y=44.7, style="t0.2c" , color="black", pen="black")
fig.plot(x=106.7, y=45.1, style="t0.2c" , color="black", pen="black")
fig.plot(x=103, y=47.8, style="t0.2c" , color="black", pen="black")
fig.plot(x=103.5, y=48.5, style="t0.2c" , color="black", pen="black")
fig.plot(x=103.2, y=50.4, style="t0.2c" , color="black", pen="black")
fig.plot(x=102.5, y=51.3, style="t0.2c" , color="black", pen="black")
fig.plot(x=102.5, y=51.9, style="t0.2c" , color="black", pen="black")
fig.plot(x=101, y=50.9, style="t0.2c" , color="black", pen="black")
fig.plot(x=99.3, y=51.2, style="t0.2c" , color="black", pen="black")
fig.plot(x=96.5, y=51.1, style="t0.2c" , color="black", pen="black")

fig.show()