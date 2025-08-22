N,K=map(int,input().split())
print(N,K)
coins=[]
for _ in range(N):
    coin=int(input())
    coins.append(coin)
coins.reverse()
answer=0
for c in coins:
    answer+=K//c
    K=K-c*(K//c)
print(answer)

