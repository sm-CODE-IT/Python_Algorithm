def solution(seoul):
    num=""
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            num=str(i)
            break
    return "김서방은 "+num+"에 있다"