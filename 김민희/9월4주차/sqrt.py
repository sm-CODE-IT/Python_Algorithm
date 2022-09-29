import math
def solution(n):
    num = math.sqrt(n)
    if num-math.floor(num) :
        return -1
    else:
        return (num+1)*(num+1)