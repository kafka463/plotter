from vpython import *
from time import *

mRadius = 0.75
wallThickness = 0.1
roomWidth = 20
roomHeight = 15
roomDepth =10

floors = box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth, wallThickness, roomDepth))
ceiling = box(pos= vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth))
leftWall = box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth))
rightWall = box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth))
backWall = box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness))

marble = sphere(radius = mRadius,color=color.red)

xPos=0
deltax = 0.1

while True:
    rate(10)
    xPos +=deltax
    if xPos>roomWidth/2-mRadius or xPos<-roomWidth/2+mRadius:
        deltax*=-1
    marble.pos = vector(xPos,0,0)