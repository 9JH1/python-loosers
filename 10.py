"""
Copyright @9JH1 ( https://9jh1.github.io )
EXT Q9
A 3 E 4
B 2 C 5
D 7 A 0
A 2 C 5 
D 1 C 6
E 4 B 3
E 5 C 2
A 7 B 0
D 4 E 3
B 1 D 6
"""
a=[0,0,0,0,0]
b="ABCDE"
d = ["Australia","Bangladesh","Canada","Denmark","England"]
for n in range(9+1):
    c=input("");
    c=c.strip().split(" ")
    for nn in range(5):
        if c[0]==b[nn]:
            a[nn]+=int(c[1])
        if c[2]==b[nn]:
            a[nn]+=int(c[3])
c=0;e=0;
for n in range(1+1):
    for nn in range(4+1):
        if a[nn]>a[c] and n==0:c=nn # simple sort
        elif n==1:
            if n==1 and nn==0:
                print(str(a[c])+" ",end="")
            elif a[nn]==a[c]:
                if e>0:
                    print(", ",end="")
                print(d[nn],end="")
                e+=1 
print("") # fix the newlines