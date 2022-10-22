from vpython import *
from time import *
import numpy as np
import math
import serial

ad = serial.Serial('/dev/cu.usbmodem1301',115200)
sleep(1)

scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad
scene.forward=vector(-1,-1,-1)
 
scene.width=600
scene.height=600
 
xarrow=arrow(lenght=2, shaftwidth=.1, color=color.red,axis=vector(1,0,0))
yarrow=arrow(lenght=2, shaftwidth=.1, color=color.green,axis=vector(0,1,0))
zarrow=arrow(lenght=4, shaftwidth=.1, color=color.blue,axis=vector(0,0,1))
 
frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))

body = cylinder(length=6,radius=0.5,opacity=0.8,pos=vector(-3,0,0))
myObj=compound([body])

roll=0
pitch=0
yaw=0

# graph
roll_graph = graph(xtitle="",ytitle="roll")
roll_curve = gcurve(color=color.red,label="roll",graph=roll_graph)
time =0 



def updateSim():

    k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
    y=vector(0,1,0)
    s=cross(k,y)
    v=cross(s,k)
    vrot=v*cos(roll)+cross(k,v)*sin(roll)
    
    frontArrow.axis=k
    sideArrow.axis=cross(k,vrot)
    upArrow.axis=vrot
    myObj.axis=k
    myObj.up=vrot
    sideArrow.length=2
    frontArrow.length=4
    upArrow.length=1

def drawGraph():
    time = time+1 
    roll_curve.plot(time,roll)  


while (True):
    try:
        while (ad.inWaiting()==0):
            pass
        dataPacket=ad.readline()
        dataPacket=str(dataPacket,'utf-8')
        splitPacket=dataPacket.split(",")
        if(len(splitPacket)==5):
            q0=float(splitPacket[1])
            q1=float(splitPacket[2])
            q2=float(splitPacket[3])
            q3=float(splitPacket[4])
    
            roll=-math.atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
            pitch=math.asin(2*(q0*q2-q3*q1))
            yaw=-math.atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3))-np.pi/2
    
            rate(100)
            updateSim()
            drawGraph()


            
    except:
        pass