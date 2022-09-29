import math

# 1  제곱근 함수 sqrt()
def solution(n):
    if n == int(math.sqrt(n))**2:
        return int((math.sqrt(n)+1)**2)
    else:
        return -1

# 2  제곱 함수 pow()
def nextSquare(n):
    sqrt = pow(n, 0.5)
    return int(pow(sqrt+1, 2)) if sqrt == int(sqrt) else 'no'

# 3  나머지 연산자 사용
def nextSquare2(n):
    return "no" if math.sqrt(n) % 1 else int((math.sqrt(n)+1)**2)

print("결과1 : {}".format(solution(121)))
print("결과2 : {}".format(nextSquare(121)))
print("결과3 : {}".format(nextSquare2(121)))