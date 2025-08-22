import sys
N=int(sys.stdin.readline())

N_list=list(input().split())
sort_N=sorted(N_list)
M=int(sys.stdin.readline())
M_list=list(input().split())

answer=[0 for _ in range(M)]
for m in range(M):
    a=0
    for i in range(len(sort_N)):
        if(M_list[m]==sort_N[i]):
            for n in N_list:
                if(M_list[m]==n): a+=1
            break
    answer[m]=a
a=""
for n in answer:
    a+=str(n)+" "
print(a)