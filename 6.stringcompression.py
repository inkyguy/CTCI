a="aaaaaaAABBB"
l=''
i=0
while(i<len(a)):
    l+=a[i]
    
    c=1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            c+=1
        else:
            break
    #if i<len(a):
    i+=c
    l+=str(c)
print(l)