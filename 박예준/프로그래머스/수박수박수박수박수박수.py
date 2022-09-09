#1 루프의 짝홀 검사
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

#2 문자열의 인덱스 슬라이싱 이용
def solution2(n):
    return ('수박'*n)[:n]

a = int(input())
print("Solution #1: " + solution(a))
print("Solution #2: " + solution2(a))