"""
Copyright @9JH1 ( https://9jh1.github.io )
EXT Q11
A 3 E 4 
B 2 C 5 
D 7 A 0 
A 2 C 5
E 4 B 3
E 5 C 2
A 7 B 0
D 4 E 3
B 1 D 6
"""


a=[]
b="ABCDE"
d=[]
# get amount of possible combos
for n in range(5):
    for nn in range(4):
        try:
            a.index(n,nn)
        except ValueError:
            if(n != nn):
                a.append([n,nn])
# clean thing
for l in a:
    if [l[1],l[0]] in a:
        a.remove([l[1],l[0]])
while True:
    c=input("");
    if c == "Done":break
    c=c.strip().split(" ")
    code = [b.index(c[0]),b.index(c[2])]
    if code in a:
        a.remove(code)
    else:
        code = [b.index(c[2]),b.index(c[0])]
        if code in a:
            a.remove(code)
for i in a:
    print(f"{b[i[0]]} versus {b[i[1]]} is missing.")