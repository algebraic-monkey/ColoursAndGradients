import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def TupleToHex(Colour):
    one = str(hex(int(Colour[0])))[2:]
    while len(one) < 2:
        one = '0' + one
    two = str(hex(int(Colour[1])))[2:]
    while len(two) < 2:
        two = '0' + two
    three = str(hex(int(Colour[2])))[2:]
    while len(three) < 2:
        three = '0' + three
    colour = str('#' + one + two +three)
    return colour

#don't input 0s; if you want to just use 1 instead

start = [255, 139, 175] #enter the start colour here in RGB form 
start_col = TupleToHex(start) 

end = [171, 227, 225] #enter the end colour here in RGB form 
end_col = TupleToHex(end)

ax.scatter(start[0], start[1], start[2], color = start_col)
ax.scatter(end[0], end[1], end[2], color = end_col)

#goal: same increment for radius and angle

start_rg = math.atan((start[1] / start[0]))
start_rg_b = math.atan((start[2] / ((start[0] ** 2 + start[1] ** 2) ** 0.5)))
start_radius = (start[0] ** 2 + start[1] ** 2 + start[2] ** 2) ** 0.5

end_rg = math.atan((end[1] / end[0]))
end_rg_b = math.atan((end[2] / ((end[0] ** 2 + end[1] ** 2) ** 0.5)))
end_radius = (end[0] ** 2 + end[1] ** 2 + end[2] ** 2) ** 0.5

STEP_rg = (end_rg - start_rg) / 50
STEP_rg_b = (end_rg_b - start_rg_b) / 50
STEP_radius = (end_radius - start_radius) / 50

for i in range(1, 50):
    new_rg = start_rg + (i * STEP_rg)
    new_rg_b = start_rg_b + (i * STEP_rg_b)
    new_radius = start_radius + (i * STEP_radius)

    new_blue = new_radius * math.sin(new_rg_b)
    new_red_green = new_radius * math.cos(new_rg_b)
    new_green = new_red_green * math.sin(new_rg)
    new_red = new_red_green * math.cos(new_rg)

    new = [new_red, new_green, new_blue]
    new_col = TupleToHex(new)
    ax.scatter(new[0], new[1], new[2], color = new_col)
    

ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')

plt.show()
