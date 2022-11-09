N, M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

queue = list(range(1, N+1))  # 원형 큐를 생성
cur = 0
for num in nums:
    index = queue.index(num)
    if len(queue) // 2 >= index:
        cur += index
    else:
        cur += len(queue) - index
    queue = queue[index + 1:] + queue[:index]
print(cur)
