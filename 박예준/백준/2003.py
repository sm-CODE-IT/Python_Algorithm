N, M = map(int, input().split(" "))
result, nums = 0, list(map(int, input().split(" ")))

# 이중 for문 - O(n^2)의 알고리즘
# for i, num in enumerate(nums):
#     sum = 0
#     for j in range(i, len(nums)):
#         sum += nums[j]
#
#         if sum == M:
#             result += 1
#             sum = 0
#             break
# print(result)

# 투 포인터 이용
N, M = map(int, input().split(" "))
result, nums = 0, list(map(int, input().split(" ")))

left, right = 0, 1
sum_num = nums[0]
while left <= right and right <= N:
    sum_num = sum(nums[left:right])   # 슬라이싱 활용
    if sum_num == M:
        result += 1
        right += 1
    elif sum_num < M:
        right += 1
    else:
        left += 1

print(result)
