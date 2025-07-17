N,K=map(int,input().split())
cards1=list(map(int,input().split()))
cards1.sort()
for c in cards1:
    if(cards1[0]+cards1[1]+c>K):cards1.remove(c)

count=0
for c in range(0,N):
    for a in range(c+1,N):
        for r in range(c+2,N):
            new=cards1[c]+cards1[a]+cards1[r]
            if(new>K):continue
            if K-new<K-count : count=new
print(count)
