from collections import deque

def solution(people, limit):
    people.sort()
    deq=deque(people)
    answer=0
    while deq:
        heavy = deq.pop() #현재 제일 무거운사람
        if deq:
            light = deq.popleft()
            if heavy+light>limit:
                deq.appendleft(light)
        answer+=1              

    return answer