"""
Copyright @9JH1 ( https://9jh1.github.io )
Dominos
6 2
5 5
4 3
5 3
5 2
2 1
4 0
4 1
5 1
3 0
2 2
0 0
"""
#a=input("").split(" ") # a[0] = first name, a[1] = second name
b = []
c = []
d = 0
for n in range(12):
    if n%2==0:
        # n is eve
        b.append(input("").split(" "))
    else:
        # n is odd
        c.append(input("").split(" "))
for n in range(2):
    for nn in range(6):
        if n==0:
            if b[nn][0] == b[nn][1]:
                if int(b[nn][0])>d:
                    d=int(b[nn][0])
        if n==1:
            if c[nn][0] == c[nn][1]:
                if int(c[nn][0])>d:
                    d=int(c[nn][0])
print(d)