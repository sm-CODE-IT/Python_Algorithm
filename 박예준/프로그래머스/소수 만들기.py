def isPrime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return 0
    return 1


def solution(nums):
    answer = 0
    left, right = 0, 1
    sum_num = nums[0]
    while left <= right and right <= len(nums):
        sum_num = isPrime(sum(nums[left:right]))
        right += 1



    return answer