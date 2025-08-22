import sys
N=int(sys.stdin.readline())
waiting_time=list(map(int,input().split()))
waiting_time.sort()
wait_sum=0
for i in range(N):
    wait_local_sum=0
    for k in range(i+1):
        wait_local_sum+=waiting_time[k]
    wait_sum+=wait_local_sum
print(wait_sum)
