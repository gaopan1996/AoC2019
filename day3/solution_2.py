"""
--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?

Your puzzle answer was 14228.


The length of the intersection is 1 to 1 with the intersection. So a dictionary works perfectly.
The intersection is a key and the length would be the value.
Find the intersection list and then find the min length at each intersection.
"""
def create_wire(path):
    wire = {}
    x = 0
    y = 0
    length = 0
    for instruction in path:
        direction = instruction[0]
        unit = int(instruction[1:])
        for i in range(unit):
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            else:
                print("oops.")
                return False

            length += 1
            if (x,y) not in wire:
                wire[(x,y)] = length
    return wire

fo = open('input.txt', 'r')
line1 = fo.readline().rstrip('\n').split(',')
line2 = fo.readline().rstrip('\n').split(',')

wire1 = create_wire(line1)
wire2 = create_wire(line2)
intersections = wire1.keys() & wire2.keys()
min_length = min([wire1[(x,y)] + wire2[(x,y)] for (x,y) in intersections])
print(min_length)
