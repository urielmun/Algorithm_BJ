import sys
N= int(sys.stdin.readline())
N_list=list(map(str,input().split()))
sort_list=['0' for _ in range(N+1)]
for i in N_list:
    for k in range(N):
        if(int(i[0])>int(sort_list[k][0])): #첫숫자 크기 비교(i가 더 큼)
            for t in range(k,0,-1): #이전의 것들 뒤로 밀기//범위 확인 必
                old=sort_list[t]
                sort_list[t+1]=old
            sort_list[k]=i[0] #i가 비어진 자리에 들어감. 
            break
        elif(int(i[0])==int(sort_list[k][0])):#첫숫자 크기가 같음
            if


    k_locate=0
    for k in sort_list:
        if(i[0]>k[0]):
            sort_list[k_locate]=i
            break
        k_locate+=1
