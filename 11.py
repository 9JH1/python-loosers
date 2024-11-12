"""
Copyright @9JH1 ( https://9jh1.github.io )
EXT Q10
"""
a=[0,0,0,0,0];b="ABCDE";e=0
for n in range(9+1):
    c=input("");g=c;c=c.strip().split(" ")
    for nn in range(4+1):
        for nnn in range(int(len(c)/2)):                                                # | Advanced stack detection
            if c[nnn+nnn] == b[nn]:                                                     # |
                a[nn] += int(c[nnn+nnn+1])                                              # |
            elif b.replace(c[nnn+nnn],"TEST")==b and nn==0:                             # |
                print(f"{c[nnn+nnn]} is incorrect on line {n+1}.");print(g);e+=1
if(e==0):
    print("There Are no errors.")
        