import sys
from PIL import Image, ImageDraw
def drawtraj(trajx,trajy,starx,stary,rmax):
    scale=2
    rsun=5
    img = Image.new("RGB",(rmax,rmax),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((-rsun+rmax/2,-rsun+rmax/2,rsun+rmax/2,rsun+rmax/2),(255,0,0))
    for i in range(len(trajx)):
        draw.point((scale*trajx[i]+rmax/2,rmax/2-scale*trajy[i]),(0,255,0))
        draw.point((scale*trajx[i]+rmax/2,rmax/2-scale*trajy[i]),(0,255,0))
        draw.point((scale*starx[i]+rmax/2,rmax/2-scale*stary[i]),(255,0,0))
    img.show()
    return
