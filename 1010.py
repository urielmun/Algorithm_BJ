min,Max=map(int,input().split())
m=min
result=[]
for n in range(min,Max+1):
    m=min
    for m in range(min,Max+1):
        if(m%n!=0):break
    if m==Max:result.append(m)
    
    


