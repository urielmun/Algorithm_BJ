remains=[]
for i in range(10):
    a=int(input())
    r=a%42
    remains.append(r)

print(len(set(remains)))