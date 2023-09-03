import matplotlib.pyplot as plt
import numpy as np

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

start = [0, 213, 255] #enter the start colour here in RGB form 
start_col = TupleToHex(start)

end = [173, 32, 0] #enter the end colour here in RGB form 
end_col = TupleToHex(end)

ax.scatter(start[0], start[1], start[2], color = start_col)
ax.scatter(end[0], end[1], end[2], color = end_col)

STEP = [(end[0] - start[0]) / 50, (end[1] - start[1]) / 50, (end[2] - start[2]) / 50]

for i in range(1, 50):
    new = [start[0] + i * STEP[0], start[1] + i * STEP[1], start[2] + i * STEP[2]]
    new_col = TupleToHex(new)
    ax.scatter(new[0], new[1], new[2], color = new_col)
    

ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')

plt.show()
