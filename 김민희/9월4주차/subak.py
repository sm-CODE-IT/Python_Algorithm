def solution(n):
    total=""
    for i in range(n):
        if i % 2==0:
            total+="수"
        else:
            total+="박"
    return total