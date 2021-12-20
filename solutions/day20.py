import os
import sys
INPUTS = os.path.join(os.path.dirname(__file__), '..', 'inputs')
INP = os.path.join(INPUTS, 'input20.txt')


def pixel(img, alg, i, j):
    rows, cols = len(img), len(img[0])
    idx = 0
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if -1 < ii < rows and -1 < jj < cols:
                if img[ii][jj] == '#':
                    idx += 1
            idx *= 2
    return alg[idx // 2]

def enhance(img, alg):
    k = 3
    img = ['.'*k + row + '.'*k for row in img]
    for _ in range(k):
        img = ['.' * len(img[0])] + img + ['.' * len(img[0])]
    rows, cols = len(img), len(img[0])
    newimg = []
    for i in range(cols):
        row = []
        for j in range(cols):
            row.append(pixel(img, alg, i, j))
        newimg.append(''.join(row))
    return newimg

def counLit(img):
    count = 0
    for row in img:
        count += row.count('#')
    return count

def showimg(img, file = sys.stdout):
    for row in img:
        for c in row:
            if c == '.':
                print(' ', end = '', file=file)
            else:
                print(c, end='', file=file)
        print(file=file)

def p1(file, n):
    with open(file) as inp:
        alg = inp.readline().strip()
        inp.readline()
        img = [l.strip() for l in inp]
    for _ in range(n):
        img = enhance(img, alg)

    # writing to file, and then visually finding image borders
    with open('IMG.pbm', 'w') as f:
        f.write(f'P1\n{len(img)} {len(img[0])}\n')
        showimg(img, f)
    print()
    return counLit(img)
print(p1(INP, 20))
