def solution(bridge_length, weight, truck_weights):
    answer = 0
    on = []
    while on or truck_weights:
        answer+=1
        for o in on:
            o[1] +=1
        if on and on[0][1] >= bridge_length:
            on.pop(0)
        if truck_weights:
            if sum([o[0] for o in on],truck_weights[0]) <= weight:
                on.append([truck_weights.pop(0),0]) 
    
    return answer