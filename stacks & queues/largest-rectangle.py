# https://www.hackerrank.com/challenges/largest-rectangle/problem
def largestRectangle(h):
    maxRec = 0
    for i in range(len(h)):
        e, e2 = i, i
        numofRectangles = 0
        while e<len(h) and h[i]<=h[e]:
            numofRectangles += 1
            e += 1
        while e2>=0 and h[i]<=h[e2]:
            numofRectangles += 1
            e2 -= 1
        curArea = h[i] * (numofRectangles-1)
        if maxRec<curArea:
            maxRec = curArea
    return maxRec