# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Wave Equation Plot program

Run '%matplotlib qt' on Spyder console
for FuncAnimation to work properly.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

Dx = 1
Dy = 1
Dt = 1/20
Dh = 1
Vel = 5.0
Const = (Dt/Dh)**2
M = 80 #Columns num (x)
N = 80 #Rows num (y)
Q = 500 #Matrix num (steps)

V=np.zeros((M,N))
w=np.zeros((M+1,N+1,Q+1))

sismo1=np.zeros(Q+1)
sismo2=np.zeros(Q+1)
sismo3=np.zeros(Q+1)
sismo4=np.zeros(Q+1)
sismo5=np.zeros(Q+1)
    
#Initialize Velocity matrix
for j in range(0,M):
    for i in range(0,N):
        V[i,j]=Vel
        if i<=30 and i>=20 and j<=30 and j>=20:
            V[i,j]=Vel*0.3
        
#Limit conditions
for k in range(0,Q+1):
    w[1,1,k] = 0.0
    w[M,N,Q] = 0.0
    
#Elastic Pulse (Earthquake origin)
for i in range (1,M+1):
    for j in range (1,N+1):
        if i <= 4:
            if j <= 4:
                w[i,j,1] = (0.5)*np.sin(i*np.pi/20)*np.sin(j*np.pi/20)
        else:
            w[i,j,1] = 0.0
        
w[:,:,2] = w[:,:,1]

for k in range(1,Q):
    for j in range(1,N):
        for i in range(1,M):
            w[i,j,k+1]= 2*w[i,j,k]-w[i,j,k-1]+(Const*(V[i,j])**2)*(w[i-1,j,k]+w[i+1,j,k]-4*w[i,j,k]+w[i,j+1,k]+w[i,j-1,k])
            
    sismo1[k]=w[4,4,k]
    sismo2[k]=w[40,40,k]
    sismo3[k]=w[4,40,k]
    sismo4[k]=w[40,4,k]
    sismo5[k]=w[8,15,k]

X, Y = np.meshgrid(range(0,M+1), range(0,N+1))

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.gca(projection='3d')


# Normalize to [0,1]
norm = plt.Normalize(-0.1, 0.1)


h = 0
def animate(i):
    global h
    h += 1
    if h == Q:
        anim.event_source.stop()
    ax1.clear()
    surf = ax1.plot_surface(X.T,Y.T,w[:,:,h], cmap=mcolors.ListedColormap(['white']), norm=norm, linewidth=1, shade=False, alpha=0.5)
    m = plt.cm.ScalarMappable(surf.norm)
    surf.set_edgecolors(m.to_rgba(surf.get_array()))
    ax1.set_proj_type('ortho')
    ax1.set_zlim(-0.5, 0.5)
    # ax1.view_init(azim=-120, elev=45)
    ax1.set_title(h)
    ax1.set_ylabel('Posición y')
    ax1.set_xlabel('Posición x')
    ax1.set_zlabel('Desplazamiento')
    ax1.plot(4,4,w[4,4,h], markerfacecolor='r', marker='o', markersize=5)
    ax1.plot(40,40,w[40,40,h], markerfacecolor='r', marker='o', markersize=5)
    ax1.plot(4,40,w[4,40,h], markerfacecolor='r', marker='o', markersize=5)
    ax1.plot(40,4,w[40,4,h], markerfacecolor='r', marker='o', markersize=5)
    ax1.plot(8,15,w[8,15,h], markerfacecolor='r', marker='o', markersize=5)

    

anim = animation.FuncAnimation(fig,animate,frames=Q+1,interval=1)

fig2, (a1, a2, a3, a4, a5) = plt.subplots(5)
fig2.suptitle('Sismica')
a1.plot(sismo1)
a2.plot(sismo2)
a3.plot(sismo3)
a4.plot(sismo4)
a5.plot(sismo5)

plt.show()