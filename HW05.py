GlowScript 3.0 VPython
## Matthew Kistner

## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# Uncomment this next line if you prefer a white background
scene.background = color.white

# Visualization (object, trail, origin)
ball = sphere(color=color.blue, radius=0.0285)
trail = curve(color=color.green, radius=0.02)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.04)

# Arrows to represent vector quantities in the visualization window
gravArrow = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.orange)
dragArrow = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.cyan)

# Graphing (if needed, you can add more plot and curve lines)
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)


#Initial Conditions and Mass
ball.m = 0.204
ball.pos = vector(1.11022302e-16, -4.854139925687395e-4,0)
ball.vel = vector(0,0,0)

#Time
t = 0
deltat = 0.01

#Magnitude of Gravity's Acceleration
g = 9.8

#Unit Vector for positive y axis
jhat = vector(0,1,0)

#Drag Constant
b = 2.085

while t < 1.077: 
    rate(200)
    Ft = -ball.m * -g * jhat
    W = ball.m * -g * jhat
    Fnet = W + Ft
    ball.vel = ball.vel + (Fnet/ball.m) * deltat
    ball.pos = ball.pos + ball.vel * deltat
    t = t + deltat
    print(t,ball.pos.y)
    
while t < 1.630: 
    rate(200) 
    Fd = -b * mag(ball.vel)**2*norm(ball.vel)
    W = ball.m * -g * jhat
    Fnet = W + Fd
    ball.vel = ball.vel + (Fnet/ball.m) * deltat
    ball.pos = ball.pos + ball.vel * deltat
    t = t + deltat
    print(t,ball.pos.y)
