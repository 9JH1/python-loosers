"""
Copyright @9JH1 ( https://9jh1.github.io )
"""
a=[0,0]
for n in range(2+1): # I hate python
    b=input("");
    if b=="Cat":a[0]+=1 # no ++ 
    elif b=="Dog":a[1]+=1
if a[1]>=2:
    print("Yay, I'm getting a dog.")
else:
    print("Awww")