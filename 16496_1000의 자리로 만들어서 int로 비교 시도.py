
N= int(input())
N_list=list(map(str,input().split()))
'''
어차피 최대 1000 이니깐, 몇자리수인지 저장한후-> 모두 1000자리 수로 바꾸자(1)
예) 9->[9000,1], 20->[2000,2]
이러면 각 리스트의 인덱스 [0]기준으로 sort하고, [1]기준으로 slice(2)
*문제:
[0]을 기준으로 sort하니깐, 3과 30을 똑같다고 생각하고 sort함.
해결:
자릿수를 제2조건으로 설정하여, [0]이 똑같을때 자릿수가 작은것부터 정렬함.  
문제:
91 9 가 입력되면, 조합을 안해서 걍 
919 로 출력함. 
정답: 991
그 후 더하면 됨. 
'''
sliced_n=[]
for n in range(N):#(1)
    length=len(N_list[n])
    N_list[n]=(N_list[n]+"000000000")[0:10]
    sliced_n.append([N_list[n],length])
#(2)
answer=""
sliced_n.sort(key=lambda x: (int(x[0]),-x[1]),reverse=True)
for i in sliced_n:
    before=i[0]
    key=i[1]
    after=before[:key]
    answer=answer+after
print(int(answer))





