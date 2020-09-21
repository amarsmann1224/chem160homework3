from math import sqrt
from drawtraj import drawtraj
def force(x,y,m,mstar):
    r2=x**2+y**2
    r32=r2*sqrt(r2)
    fx=-x*m*mstar/r32
    fy=-y*m*mstar/r32
    return fx,fy
def integrate(x,y,vx,vy,fx,fy,m,dt,x1,y1,vx2,vy2,mstar):
    ax,ay=fx/m,fy/m
    vx+=ax*dt
    vy+=ay*dt
    x+=vx*dt
    y+=vy*dt
    ax2,ay2= fx/mstar,fy/mstar
    vx2 +=ax2*dt
    vy2 +=ay2*dt
    x1 +=vx2*dt
    y1 +=vy2*dt
    return x,y,vx,vy,x1,y1,vx2,vy2
# Main part of the program
mstar=100
m=1
nsteps=100000
dt=0.01
r=50
x,y=0,r
x1,y1=0,0
vx,vy=1.2,0
vx2,vy2=0,0
trajx,trajy=[],[]
starx,stary=[],[]
for t in range(nsteps):
    fx,fy=force(x,y,m,mstar)
    x,y,vx,vy,x1,y1,vx2,vy2=integrate(x,y,vx,vy,fx,fy,m,dt,x1,y1,vx2,vy2,mstar)
    trajx.append(x)
    trajy.append(y)
    starx.append(x1)
    stary.append(y1)
drawtraj(trajx,trajy,starx,stary,6*r)
