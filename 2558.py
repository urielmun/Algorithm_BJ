import math
T_io=[]
T=int(input())
for _ in range(T):
    c_list=[]
    count=0
    x1,y1,x2,y2=map(int,input().split())
    start=(x1,y1)#출발점
    end=(x2,y2)#도착점
    n=int(input())#행성계
    for _ in range(n):
        c=list(map(int,input().split()))
        cc=(list[0],list[1])
        r=list[3]
        d1=math.dist(start,cc)
        d2=math.dist(end,cc)
        if(d1<r or d2<r):
            count+=1
    T_io.append(count)
for i in T_io:
    print(i)
    



