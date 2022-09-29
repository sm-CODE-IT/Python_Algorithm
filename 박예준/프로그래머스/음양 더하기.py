def solution(absolutes, signs):
    result = 0
    for i in range(len(signs)):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result

# 2  튜플의 형태로 반환하는 zip 함수를 사용 -> 두 배열이 일대일 대응된다는 점을 이용
def solution2(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))


print("결과 : {}".format(solution([18, 2, 10], [True, False, False])))
print("결과 : {}".format(solution2([18, 2, 10], [True, False, False])))