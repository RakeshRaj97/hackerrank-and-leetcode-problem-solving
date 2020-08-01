# https://www.hackerrank.com/challenges/game-of-two-stacks/problem

def twoStacks(x, a, b):
    s, i, j = 0, 0, 0
    while i<len(a) and s+a[i]<=x:
        s += a[i]
        i += 1
    c = i
    while j<len(b) and i>=0:
        s += b[j]
        j += 1
        while s>x and i>0:
            i -= 1
            s -= a[i]
        if s<=x and i+j>c:
                c = i+j
    return c
