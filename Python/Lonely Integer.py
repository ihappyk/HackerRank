def lonelyinteger(b):
    answer = 0
    for i in b:
        answer = i ^ answer    
    return answer