# 대문자로 이루어진 영문 이름을 입력받아 알파벳 순서를 적절히 바꾸고, 팰린드롬을 만드는 코드

name = input()
name_list = []

# 문자열 -> 문자 배열로 바꾸기
for n in name:
    name_list.append(n)

# 리스트 -> 집합으로 변환한 후, 집합 내의 요소 개수가 홀수인 원소는 0 또는 1개인지 검사한다. 
name_set = set(name_list)

cnt = 0   # 홀수 개수
result = ""
for n in name_set:
    if cnt >= 2:
        result = "I'm Sorry Hansoo"
        break
    if name_list.count(n) % 2 != 0:   # 개수가 홀수인 것이 있다면 가운데 인덱스로 insert 나중에
        cnt += 1
        name_list.remove(n)
        name_list.insert(len(name_list)//2, n)

for n in range(0, len(name_list)-1):
    if name_list[n] < name_list[n+1]:
        print(1)
print(result)