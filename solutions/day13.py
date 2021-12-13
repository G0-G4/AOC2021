'''
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?


--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?

'''

import os
INPUTS = os.path.join(os.path.dirname(__file__), '..', 'inputs')
INP = os.path.join(INPUTS, 'input13.txt')


def fold(ax, n, paper):
    rows, cols = len(paper), len(paper[0])
    if ax == 'y':
        for y in range(n, rows):
            for x in range(cols):
                paper[2 * n - y][x] = paper[2 * n - y][x] or paper[y][x]
        del paper[n :]

    if ax == 'x':
        for y in range(rows):
            for x in range(n, cols):
                paper[y][2 * n - x] = paper[y][2 * n - x] or paper[y][x]
        
        for _ in range(rows):
            del paper[_][n :]

def count(paper):
    k = 0
    for y in range(len(paper)):
        for x in range(len(paper[0])):
            k += paper[y][x]
    return k

def paperPrint(paper):
    for row in paper:
        print(''.join(map(lambda x: '#' if x else ' ', row)))

def p1(file):
    with open(file) as inp:
        l = ''
        dots = []
        instructions = []

        Mx, My = 0, 0
        l = inp.readline()
        while l != "\n":
            x, y = map(int, l.strip().split(','))
            Mx = max(Mx, x)
            My = max(My, y)
            dots.append((x, y))
            l = inp.readline()

        paper = [[False] * (Mx + 1) for _ in range(My + 1)]
        for x, y in dots:
            paper[y][x] = True

        for l in inp:
            ax, n = l.split()[-1].split('=')
            n = int(n)
            instructions.append((ax, n))
        
    fold(*instructions[0], paper)
    return count(paper)



def p2(file):
    with open(file) as inp:
        l = ''
        dots = []
        instructions = []

        Mx, My = 0, 0
        l = inp.readline()
        while l != "\n":
            x, y = map(int, l.strip().split(','))
            Mx = max(Mx, x)
            My = max(My, y)
            dots.append((x, y))
            l = inp.readline()

        paper = [[False] * (Mx + 1) for _ in range(My + 1)]
        for x, y in dots:
            paper[y][x] = True

        for l in inp:
            ax, n = l.split()[-1].split('=')
            n = int(n)
            instructions.append((ax, n))

    for inst in instructions: 
        fold(*inst, paper)
    paperPrint(paper)

print(p1(INP))
p2(INP)