import math
N=int(input())
answer=[]
for i in range(N):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    
        
    d=math.dist((x1,y1),(x2,y2))
    print(d)

    if(x1==x2 and y1==y2):
        if(d!=r1+r2):
            answer.append(0)
            break
        elif(d==r1+r2):
            answer.append(-1)
            break
    if(d<r1+r2):answer.append(2)
    elif(d==r1+r2):answer.append(1)
    elif(d>r1+r2):answer.append(0)
    print(answer)
for i in answer:
    print(i)
