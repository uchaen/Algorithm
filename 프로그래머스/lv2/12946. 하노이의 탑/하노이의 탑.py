def solution(n):
    def hanoi(start,tmp,end,h):
        if h==2:
            answer.append([start,tmp])
            answer.append([start,end])
            answer.append([tmp,end])
        else:            
            hanoi(start,end,tmp,h-1)
            answer.append([start,end])
            hanoi(tmp,start,end,h-1)
    answer = []
    hanoi(1,2,3,n)
    return answer