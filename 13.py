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

5 5 
6 6 
4 4
5 3
4 3
5 2
4 2
5 1
4 0
5 0
3 2
4 1
"""
a = {
    "0":[],
    "1":[]
}
b=0
c= input("").split(" ")
d=""
e = []

for n in range(12):
    if n%2==0:
        a["0"].append(input("").split(" "))
    else:
        a["1"].append(input("").split(" "))
for n in range(2):
    for nn in range(6):
        if(n==0):
            l = int(a["0"][nn][0]+a["0"][nn][1])
            if l>b:
                b=l
                d = c[n]
        if(n==1):
            l = int(a["1"][nn][0]+a["1"][nn][1]);
            if l>b:
                b=l
                d = c[n]
for n in range(6):
    if c.index(d) == 0:
        if a["1"][n][0] == str(b)[0] or a["1"][n][0]  == str(b)[1] or a["1"][n][1] == str(b)[0] or a["1"][n][1]==str(b)[1]:
            e=a["1"][n]
    elif c.index(d) == 1:
        if a["0"][n][0] == str(b)[0] or a["0"][n][0]  ==str(b)[1] or a["0"][n][1] == str(b)[0] or a["0"][n][1]==str(b)[1]:
            e=a["0"][n]

if e!=[]:
    if c.index(d) == 0:
        print(f"{c[1]} should play tile {e[0]}, {e[1]}.")
    elif c.index(d) == 1:
        print(f"{c[0]} should play tile {e[0]}, {e[1]}.")
else:
    if c.index(d) == 0:
        print(f"{c[1]} can't go.")
    elif c.index(d) == 1:
        print(f"{c[0]} can't go.")