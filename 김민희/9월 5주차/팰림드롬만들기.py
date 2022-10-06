#리스트로 변환
strs=list(input())
#팰림드롬 넣을 리스트
result=[]
#for 알파벳 순서대로 출력 -> 정렬
strs.sort()
#같은 문자열 찾기
def isSame(lst):
    count={}
    for i in lst:
        try:count[i]+=1
        except:count[i]=1
    return count

#홀수 개수 판별
def isOdd(ls):
     cnt=0
     for i in range(len(ls)):
        if(ls[i]%2!=0):
            cnt+=1
     if(cnt>1):
        return False
     else:
        return True



count=isSame(strs)
#딕셔너리의 값만 모음
#따라서 특정 인덱스에 접근하기 위해서는 dict.values를 리스트로 변환한 후 값에 접근해야 한다.
val=list(count.values())
#딕셔너리의 key 모음
key=list(count.keys())

if(isOdd(val)):
    for i in range(len(val)):
            for j in range(val[i]//2):
                 result.append(key[i])
    #알파벳 모두 짝수개
    if(len(strs)%2==0):
        result=''.join(result)
        r_result=''.join(reversed(result))
        print(result+r_result)
    #알파벳 한 개만 홀수개
    else:
        for i in range(len(val)):
            if(val[i]%2!=0):
                odd=[key for key, value in count.items() if value == val[i]]
        result=''.join(result)
        r_result=''.join(reversed(result))
        odd=''.join(odd)
        print(result+odd+r_result)

#홀수가 2개 이상이면 팰린드롬x
else:
    print("I'm Sorry Hansoo")
   
#68ms