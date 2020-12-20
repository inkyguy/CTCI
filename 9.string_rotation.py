def rot(b,a):
    if len(a)!=len(b):
        return False
    n=len(a)

    for i in range(n):
        k=a[i:]+a[:i]
        if k==b:
            return True
    return False

def alterlogic(a,b):
    k=b+b
    return a in k
print(rot("waterbottle","erbottlewat"))
print(alterlogic("waterbottle","erbottlewat"))