from collections import Counter

def perm(a,b):
    if len(a)!=len(b):
        return False
    c=Counter()
    for i in a:
        c[i]+=1
    for j in b:
        if c[j]==0:
            return False
        c[j]-=1
    return True
print(perm("avohailbcc","aohacbvilc"))
