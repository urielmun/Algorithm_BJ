#문자열로 입력받은 뒤 
word=input()
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer=[]
#리스트를 for문으로 순회하며, find함수 사용
#find 함수 설명-> https://easyjwork.tistory.com/3
for a in alphabet:
    answer.append(word.find(a))
for a in answer:
    print(a,end=' ')