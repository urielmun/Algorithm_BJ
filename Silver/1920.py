N=int(input())
N_list=list(map(int,input().split()))

M=int(input())
M_list=list(map(int,input().split()))

answer=[]
A=set(N_list)
for m in M_list:
    if m in A:
        print(1)
    else:
        print(0)