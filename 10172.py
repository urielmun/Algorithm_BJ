row,col=map(int,input().split())
A=[]
B=[]
for i in range(row):
    a=list(map(int,input().split()))
    A.append(a)
for i in range(row):
    b=list(map(int,input().split()))
    B.append(b)  
Sum=[[]]
for r in range(row):
    for c in range(col):
        print(A[r][c]+B[r][c],end=" ")
    print(" ")
        
    





