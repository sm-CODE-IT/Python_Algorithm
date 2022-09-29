def solution(num):
    # num은 파라미터로 받기 때문에 바로 검사한다. 
    if num == 1:
        return 0

    cnt = 0  # 루프의 반복 횟수 카운트

    while (num != 1):
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        cnt += 1

        # cnt의 예외 검사는 한 번의 루프를 돌아 갱신된 값이 반영된 이후에 검사
        if cnt >= 500:
            return -1

    return cnt