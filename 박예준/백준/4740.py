### 아스키 코드값을 가지는 문자에 대해서만 거꾸로 출력하는 문제
from sys import stdin

while True:
    word = input()
    if word == "***":
        break

    print(word[::-1])