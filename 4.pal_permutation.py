from collections import Counter

def palperm(a):
    a=a.replace(' ','')
    if a==a[::-1]:
        return True
    c=Counter()
    for i in a:
        c[i]+=1
    v=list(c.values())    
    if len(a)%2==0:
        for i in c.values():
            if i%2!=0:
                return False
        return True
    else:
        if v.count(1)==1:
            v.remove(1)
            for i in v:
                if i%2!=0:
                    return False
            return True

print(palperm("abb"))

