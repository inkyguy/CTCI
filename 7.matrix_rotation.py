m = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

r=[[0]*3]*3
print(r)
for i in range(3):
  for j in range(3):
    r[i][j]=m[j][i]
  r[i]=r[i][::-1]
print(r)