'''
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

To begin, get your puzzle input.

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
'''
import os
INPUTS = os.path.join(os.path.dirname(__file__), '..', 'inputs')
INP = os.path.join(INPUTS, 'input9.txt')

def p1(file):

    heightmap  = []
    with open(file) as inp:
        for l in inp:
            heightmap.append(list(map(int, list(l.strip()))))
        
    s = 0

    rows, cols = len(heightmap), len(heightmap[0])
    for i in range(rows):
        for j in range(cols):
            left = top = right = bottom = 10
            if i > 0:
                top = heightmap[i - 1][j]
            if i < rows - 1:
                bottom = heightmap[i + 1][j]
            if j > 0:
                left = heightmap[i][j - 1]
            if j < cols - 1:
                right = heightmap[i][j + 1]
            
            el = heightmap[i][j]
            if (el < right and el < left and
                el < top and el < bottom):
                s += el + 1 
    
    return s


def basin(rows, cols, i, j, h,  b = set()):
    
    b.add((i, j))
    if h[i][j] == 9: return 0
    count = 1

    if (i + 1, j) not in b and i < rows - 1:
        count += basin(rows, cols, i + 1, j, h, b)

    if (i - 1, j) not in b and i > 0:
        count += basin(rows, cols, i - 1, j, h, b)

    if (i, j + 1) not in b and j < cols - 1:
        count += basin(rows, cols, i, j + 1, h, b)

    if (i, j - 1) not in b and j > 0:
        count += basin(rows, cols, i, j - 1, h, b)

    return count


def p2(file):

    heightmap  = []
    with open(file) as inp:
        for l in inp:
            heightmap.append(list(map(int, list(l.strip()))))
        
    s = 0
    M = [-1, -1, -1]
    rows, cols = len(heightmap), len(heightmap[0])
    for i in range(rows):
        for j in range(cols):
            left = top = right = bottom = 10
            if i > 0:
                top = heightmap[i - 1][j]
            if i < rows - 1:
                bottom = heightmap[i + 1][j]
            if j > 0:
                left = heightmap[i][j - 1]
            if j < cols - 1:
                right = heightmap[i][j + 1]
            
            el = heightmap[i][j]
            if (el < right and el < left and
                el < top and el < bottom):

                size = basin(rows, cols, i, j, heightmap)
                if size > M[2]:
                    M = M[1:] + [size]
                elif size > M[1]:
                    M = [M[0]] + [size] + [M[2]]
                elif size > M[0]:
                    M[0] = size
                    
    return M[0] * M[1] * M[2]
        


print(p1(INP))
print(p2(INP))