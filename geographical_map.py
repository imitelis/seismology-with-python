import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import matplotlib.pyplot as plt
from matplotlib.image import imread
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

vt = pd.read_csv('VECT.dat')
vt.head()
St=vt.Est
Xv=vt.Lon
Yv=vt.Lat
Dx=vt.Vcx
Dy=vt.Vcy
N=Xv.size
fallas = r'fallas.shp'
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-85, -65, -5, 15], crs=ccrs.PlateCarree())
shape_feature = ShapelyFeature(Reader(fallas).geometries(), ccrs.PlateCarree(), edgecolor='black', linewidth=0.5)
ax.add_feature(shape_feature)
ax.add_feature(cfeature.LAND, alpha=0.5)
ax.add_feature(cfeature.OCEAN, alpha=0.5)
ax.add_feature(cfeature.COASTLINE, color='blue', linewidth=0.3)
ax.add_feature(cfeature.BORDERS, linewidth=0.3)
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS, color='gray',linewidth=0.3)
source_proj = ccrs.PlateCarree()
fmap = 'topo_base_Geomapapp.tif'
ax.imshow(imread(fmap), origin='upper', transform=source_proj, extent=[-85, -60, -5, 15])
#ax.stock_img()
plt.scatter(X,Y,s=M/2,c='r',alpha=0.5)
plt.scatter(Xv,Yv,alpha=0.5)
plt.quiver(Xv,Yv,Dx,Dy)
plt.show()

fig.savefig('mimapa.tif', format='tif', dpi=1200)
