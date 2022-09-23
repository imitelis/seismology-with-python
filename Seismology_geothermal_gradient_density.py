#Seismology, density at given depth with geothermal gradient

cet = 2.4/100000
print("Please, introduce the Geothermal Gradient (°C/km): ")
GG=float(input())
print("Please, introduce the surficial density (g/cm**3): ")
rhos=float(input())
#Surface temperature
print("Please, introduce the depth of your interest (km): ")
depth=float(input())
dT=GG*depth
nrho=rhos*(1-cet*dT)
print("New density at ",depth,"is ", nrho)
