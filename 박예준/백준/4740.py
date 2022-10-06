### 아스키 코드값을 가지는 문자에 대해서만 거꾸로 출력하는 문제
from sys import stdin

while True:
    word = input()
    if word == "***":
        break

    print(word[::-1])

'''
[풀이 설명]
- left, right 두 포인터로 두 위치의 요소를 바꿔주는 방식으로 접근
- 역순으로 바꾸는 함수 정의(None 반환)
- 이를 문자열로 바꿔서 출력하기 위해 ''.join()을 이용
'''