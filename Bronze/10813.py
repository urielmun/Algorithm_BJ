N,M=map(int,input().split())
num=[]
for i in range(N):
    num.append(i+1)
for _ in range(M):
    a,b=map(int,input().split())
    switch=num[a-1]
    num[a-1]=num[b-1]
    num[b-1]=switch
for i in num:
    print(i,end=" ")
