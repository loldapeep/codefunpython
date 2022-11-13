n=int(input())
k=n-1;m=2*n;s=1;t=1
for i in range (1,k+1): s*=i
for j in range (m, m-k, -1): t*=j
print(t//s)