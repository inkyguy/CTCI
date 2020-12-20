m = [
            [1, 0, 3],
            [4, 5, 6],
            [7, 8, 1],
        ]
row=[0]*3
col=[0]*3
for i in range(3):
  for j in range(3):
    if m[i][j]==0:
      row[i]=1
      col[j]=1
for i in range(3):
  for j in range(3):
    if row[i]==1 or col[j]==1:
      m[i][j]=0

for i in m:
  print(i)