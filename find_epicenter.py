from pylab import *
import numpy as np
import random
from obspy.core import UTCDateTime
from obspy.taup import TauPyModel
model = TauPyModel(model="iasp91")

f=open("/home/cogito/Desktop/Estaciones_RSSB.txt", "r")

#Stations names
#Vector for storing X data from each station
NN=[] 
XX=[] 
YY=[]
ZZ=[]
PP=[]
SS=[]
SP=[]
xh=[]
yh=[]
zh=[]
Tp=[]
Ts=[]
Tsp=[]
i=0

for line in f:
    line = line.strip()
    columns = line.split()
    nombre = columns[0]
    x = float(columns[1])
    y = float(columns[2])
    z = -float(columns[3])/1000
    PA = float(columns[4])
    PM = float(columns[5])
    PD = float(columns[6])
    Ph = float(columns[7])
    Pm = float(columns[8])
    Ps = float(columns[9])
    Sh = float(columns[10])
    Sm = float(columns[11])
    Ss = float(columns[12])
    Pol = columns[13]    

print(nombre, x, y, z, Ph, Pm, Ps, Sh, Sm, Ss, Pol)
NN.append([nombre])
XX.append(x)
YY.append(y)
ZZ.append(z)
#PP.append(3600*(Ph-1)+60*(Pm-1)+Ps)
#SS.append(3600*(Sh-1)+60*(Sm-1)+Ss)
#SP.append(SS[i]-PP[i])
Tp.append(UTCDateTime(int(PA), int(PM), int(PD), int(Ph), int(Pm), int(Ps)))
Ts.append(UTCDateTime(int(PA), int(PM), int(PD), int(Sh), int(Sm), int(Ss)))
Tsp.append(Ts[i]-Tp[i])
i+=1
TR = min(Tp)
Tss = []
Tpp = []

xh.append(random.uniform(min(XX),max(XX)))
yh.append(random.uniform(min(YY),max(YY)))
#zh.append(random.uniform(0,111))
zh.append(1.0)
xx=np.array(XX)
yy=np.array(YY)
zz=np.array(ZZ)

k=1
rms=100
N=1000
RMS=[]

#We apply Wadati
for ii in range(i):
    Tss.append(Ts[ii]-TR)
    Tpp.append(Tp[ii]-TR)
#m,b = polyfit(SP, SS, 1)
m,b = polyfit(Tsp, Tpp, 1)
print(m, b)
To = TR+b
print('Origin Time: ',To)
a=np.array(Tsp)
p=np.array(Tpp)-b
s=np.array(Tss)-b
plot(Tsp, Tpp, 'yo', Tsp, m*a+b, '--k') 
show()

while (rms > 0.5):
    zh.append(float(k-1))
    arrivalP=[]
    d=np.power((np.power(xx-xh[k-1],2)+np.power(yy-yh[k-1],2)),0.5)
    for i in d:
        arrivals = model.get_travel_times(source_depth_in_km=zh[k-1],distance_in_degree=i)
        #print(arrivals[0])
        arrivalP.append(arrivals[0].time)
    r=arrivalP-p
    dT_dx=r/((xh[k-1]-xx)*111)
    dT_dy=r/((yh[k-1]-yy)*111)
    dT_dz=r/((zh[k-1]-zz))
    A=np.ones((len(d), 4))

for i in range (0, len(d)):
    A[i,1]=dT_dx[i]
    A[i,2]=dT_dy[i]
    A[i,3]=dT_dz[i]
    A=-A
    #dh=-np.linalg.inv(A.T@A)@A.T@r
    #For showing convergence effects, vary theta, 0.001, 0.1, 10, ...
    theta=10
    theta2=np.power(theta,2)
    I=np.identity(4)
    dh=-np.linalg.inv(A.T@A+theta2*I)@A.T@r
    #print(dh)
    xh.append(xh[k-1]+dh[1]/111)
    yh.append(yh[k-1]+dh[2]/111)
    zh.append(zh[k-1]+dh[3])
    p=p+dh[0]
    rms=np.power(sum((np.power((arrivalP-p),2))/len(d)),0.5)
    print(rms, k)
    RMS.append(float(rms))
    k=k+1
    if k == N:
        break

i=range(0,len(RMS))
plot(i[1:100],RMS[1:100],'ro')
