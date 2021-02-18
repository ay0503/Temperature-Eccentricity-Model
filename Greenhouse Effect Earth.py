from math import *
from vpython import *

#
# Because the force is different if the alpha is outside or inside the gold
# nucleus, we will use a function to compute the force. You need to code up
# both cases here for the force between part1 and part2
#
def force(part1,part2):
    if ( mag(part1.pos-part2.pos) >= part2.radius ) :
        force = 
    else:
        force = 0
    return force
#
scene2=canvas(title='Rutherford Scattering',caption='Caption',center=vector(0,0,0))
#
# Mass of the Gold:      3.35e-25 kg
# Radius of the Gold:    5.0e-14
# Mass of the Alpha:     6.8e-27 kg
# Radius of the Alpha   1e-15 m
# Kinetic Energy of the Alpha    1.6e-12 Joules
#
#  size is a scale factor that we use. Don't change
#
size=4.0e-13
#
# Initialzie parameters:
# Kinetic Energy of alpha in Joules
#
GoldRadius  = 0
AlphaRadius = 0
AlphaEnergy = 0
ImpactParameter = 0
scene2.caption=('Impact parameter=',ImpactParameter)
#
# Electric Force Constant
#
k      = 0
elechg = 0
#
# Initialize time to zero, and set a time step (seconds)
t  = 0
dt = 1.0e-23
#
#   Creae the Alpha Particle
#
alpha = sphere(pos=vector(-0.95*size,ImpactParameter,0), radius=AlphaRadiue, color=color.red)
gold = sphere(pos=vector(0,0,0), radius=GoldRadius,color=color.yellow,opacity=0.25)
#
#   You need to fill in reasonable values
#
alpha.mass   = 0
alpha.charge = 0*elechg 
alpha.energy = AlphaEnergy 
p_alpha = (2.0*alpha.mass*alpha.energy)**0.5 # Non-relativistic
#
alpha.momentum = vector(p_alpha,0,0)
alpha.velocity = vector(p_alpha/alpha.mass,0,0)
#
print('Alpha mass = ',alpha.mass)
print('Alpha momentum = ', alpha.momentum)
print('Alpha Velocity = ', alpha.velocity)
#
# Put in reasonable values
#
gold.momentum=vector(0,0,0)
gold.mass = GoldMass
gold.charge = 0 * elechg
#
#  Commands to set up a graph.....
#
s='<b>Rutherford </b>'
graph(title=s, xtitle='Time', ytitle='Angular Momentum', xmin=0, xmax=6*size, ymax=15, ymin=-5)
#
gold.trail = curve(color=gold.color) 
alpha.trail = curve(color=alpha.color)
#
runit = 1
#
while (runit==1):
#
    rate(100)
#
# Calculate the force exerted on the alpha by the gold. If
# the alpha is outside the gold, it is coulomb, inside it
# is linear.
#
    alpha.force = force(alpha,gold)
#
#  Update Mometum and positions
# 
    alpha.momentum = 0 
    alpha.pos = 0 
#
    gold.momentum = 0
    gold.pos = 0
#
    alpha.trail.append(pos=alpha.pos)
    gold.trail.append(pos=gold.pos)
#
    t = t+dt
#
#  This is a stopping condition that if we get farther away than size,
#  we stop, or if we are running forever.
#
    if(mag(alpha.pos)>size):
        runit=0
    if(t>10):    # if more than 10 seconds have passed, we have a problem.
        runit=0
#
# Add stuff below after we have stopped looping
#
theta = atan2(alpha.pos.y,alpha.pos.x)*57.3
scene2.caption=('Impact parameter=',b,' Scattering angle =',theta)
#