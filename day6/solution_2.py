"""
--- Part Two ---
Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:

    K to J
    J to E
    E to D
    D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)

Your puzzle answer was 472.


Santa's path and your path will coincide at some point. So find the number of planets that both paths share.
The length of your path minus the shared_planets is the distance to the planet you and Santa share.
The length of Santa's path minus the shared_planets is the distance to the planet you and Santa share.
So if you add both lengths up and minus the shared planet and the planet you were originally on will give you your total jumps.
"""
def find_path(node, orbits):
    return (find_path(orbits[node], orbits) if node in orbits else []) + [node]

arr = open('input.txt').read().strip().split("\n")
data = [ datum.split(")") for datum in arr ]
orbits = {satellite: planet for planet, satellite in data}

santa_path = find_path("SAN", orbits)
my_path = find_path("YOU", orbits)
shared_planets = len(list(set(my_path) & set(santa_path)))
print(len(my_path) + len(santa_path) - shared_planets * 2 - 2) 

