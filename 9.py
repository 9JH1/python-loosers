"""
Copyright @9JH1 ( https://9jh1.github.io )
bulk figure sort
A 3 E 4 
B 2 C 5 
D 7 A 0 
A 4 C 3 
D 1 C 6 
E 4 B 3 
E 5 C 2 
A 7 B 0 
D 4 E 3 
B 1 D 6 
"""
a=[0,0,0,0,0]
b="ABCDE"
for n in range(9+1):
    c=input("");
    c=c.strip().split(" ")
    for nn in range(5):
        if c[0]==b[nn]:
            a[nn]+=int(c[1])
        if c[2]==b[nn]:
            a[nn]+=int(c[3])
print(f"A {a[0]}\nB {a[1]}\nC {a[2]}\nD {a[3]}\nE {a[4]}\n",end=" ")