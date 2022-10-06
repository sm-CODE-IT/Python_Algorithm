def solution(phone_number):
    phone=""
    for i in range(len(phone_number)):
        if i<len(phone_number)-4:
            phone += "*"
        else:
            phone+=phone_number[i]
    return phone
