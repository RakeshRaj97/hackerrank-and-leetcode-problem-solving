# https://www.hackerrank.com/challenges/simple-text-editor/problem
s = ''
prev = []
for i in range(int(input())):
    query = list(input().split(' '))
    if query[0] == '1':
        prev.append(s)
        s = s+query[1]
    elif query[0] == '2':
        prev.append(s)
        s = s[0:len(s)-int(query[1])]
    elif query[0] == '3':
        print(s[int(query[1])-1])
    else:
        s = prev.pop()
