def solution(num):   
        for i in range(500):
            if i != 499 :
                if num != 1:
                    if(num%2==0):
                        num/=2
                    else:
                        num= num*3+1
                else :
                    return i
                    break
            else:
                return -1
