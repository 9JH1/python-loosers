"""
Copyright @9JH1 ( https://9jh1.github.io )
badly worded exception sort
"""
a=[0,0,0,0]
for n in range(int(input(""))):
    b=input("")
    if b=="Dog":a[0]+=1
    elif b=="Cat":a[1]+=1
    elif b=="None":a[2]+=1 
    else:a[3]+=1
print(f"{a[0]} prefer dogs.\n{a[1]} prefers cats.\n{a[2]} prefer neither cats nor dogs.\nThere was {a[3]} invalid response.\n",end="")