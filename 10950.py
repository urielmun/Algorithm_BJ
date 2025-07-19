cro_list=["c=","c-","dz=","d-","lj","nj","s=","z="]
sum=0
word=input()
i=0
while(1):
    tryy=word[i]+word[i+1]
    for k in cro_list:
        if k==tryy: sum+=1
    tryyy=word[i]+word[i+1]+word[i+2]
    if(tryyy=="dz="):sum-=1
    i+=1
    if(i==len(word)-1):break
print(sum)
    
