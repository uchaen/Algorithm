def solution(cap, n, deliveries, pickups):
    delivery = 0
    pickup = 0
    answer = 0
    
    for i in range(-1,-n-1,-1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += 2*(n+i+1)
    
    return answer