min,Max=map(int,input().split())
result=[]
remember=0
for n in range(min,Max+1):  
    for m in range(2,n):
        if(n%m==0):
            print(n,m)
            break
        if(n%m!=0 and m==n-1):
            result.append(n)

for r in result:
    print(r)

    


