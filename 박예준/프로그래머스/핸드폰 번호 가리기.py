def hide_number(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]

print(hide_number("01012345678"))