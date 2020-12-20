from collections import Counter
c=Counter()
a="bale"
b="pale"
a=set(a)
b=set(b)
k= (len(a.symmetric_difference(b)))
if (k==0 or k==1 or k==2):
  print( True)
else:
  print(False)