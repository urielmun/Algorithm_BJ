A,B=map(int,input().split())
C=int(input())
h=C//60
m=C%60

a=A+h
b=B+m


if(b>=60):
    a+=1
    b-=60
if(a>=24):
    a=a-24
print(a,b)