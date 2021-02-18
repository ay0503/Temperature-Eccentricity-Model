from math import *
from vpython import *

scene2 = canvas(title='Earth Orbiting the Sun',caption='Animated Display',center=vector(0,0,0), background=color.black)

#constantswirl 
Ts = 5778
Rs = 6.96e8
Re = 6.37e6
D  = 1.496e11

sun_earth_distance =  152095295000 #147091144000
ra = sun_earth_distance
speed_of_earth = 2 * 3.14 * sun_earth_distance / 3.15e7

earth = sphere(pos=vector(sun_earth_distance,0,0),radius=1e9,color=color.green)
sun   = sphere(pos=vector(0,0,0),radius=5e9,color=color.yellow)


G = 6.67e-11

earth.mass = 5.972e24 
sun.mass   = 1.989e30

Tge = +33
a = earth.pos.x


earth.momentum = 0.96592 * earth.mass * vector(0,speed_of_earth,0) #0.9596
sun.momentum = sun.mass * vector(0,0,0)

earth.trail = curve(color=color.magenta)
earth.trail.append(pos=earth.pos)

earth.point = arrow(pos=earth.pos,color=earth.color,axis=-norm(earth.pos))
scale = 1e-12

time = 0
dt = 12 * 3600
year = 3.6e7

tempplot = graph(title='Temperature by Time in Year',xtitle='Date',ytitle='Temperature (K)', xmin=0,
                   xmax=365, ymin=270, ymax=300, scale = 1 / 24 / 3600)

drawTe = gcurve(color=color.orange,label='Temperature')

Tedata = []
posdata = []
rp = 0
MaxSpeed = 0
MinSpeed = 0

while time < 3.1e7:
    rate(100)

    time += dt
    SED = mag(earth.pos - sun.pos)
    
    rhat = vector(sun.pos - earth.pos) / SED
    earth.force = (G * earth.mass * sun.mass / SED ** 2) * rhat 
    
    earth.momentum = earth.momentum + earth.force * dt
    earth.velocity = earth.momentum / earth.mass
    earth.speed = mag(earth.velocity)
    earth.pos = earth.pos + earth.velocity * dt
    
    posdata.append(earth.pos.y)
    
    if earth.speed > MaxSpeed:
        MaxSpeed = earth.speed
        rp = mag(earth.pos - sun.pos)   

    #Stefan-Boltzmann Law
    Te = (0.7 ** 0.25) * Ts * (Rs / (2 * SED)) ** 0.5 + Tge
    
    date = time / 24 / 3600
            
    E = (ra - rp)/(ra + rp)
          
    earth.trail.append(pos=earth.pos)
    earth.point.pos = earth.pos
    earth.point.axis = earth.force * scale
        
    drawTe.plot(pos=(date,Te))    
    Tedata.append(Te)

print(ra, rp)
print("Orbital Statistics")
print("Eccentricity = ",E)    
print("Temperature Average = ", sum(Tedata)/len(Tedata)) 