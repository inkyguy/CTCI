def unique(s):
    if len(s)>128:
        return False
    chset=[False]*128
    for i in s:
        k=ord(i)
        if chset[k]:
            return False
        chset[k]=True
    return True

print(unique("Soohail")) 
print(unique("23jsdfm2"))