#1 문자열 이어붙이기 연산자 '+' 사용
def solution(seoul):
    x = seoul.index("Kim")
    return "김서방은 " + str(x) + "에 있다"

#2 format 함수 사용
def solution2(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))

arr = ["Park", "Ye", "Jun", "Kim"]
print(solution(arr))
print(solution2(arr))