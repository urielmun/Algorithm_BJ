N=int(input())
answer=0
len_N=len(str(N))
for compare in range(int(10^(len_N-1)),int(10^(len_N))):
    str_compare=str(compare)
    sum_=0
    for k in range(len_N-1):
        sum+=int(compare[k])
    if(compare+sum==N):
        answer=compare
        break
print(answer)

        



