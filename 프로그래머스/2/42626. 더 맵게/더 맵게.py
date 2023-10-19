import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    if scoville[1] ==0: return -1 #애초에 못만듦

    answer=0
    while(1):
        if scoville[0] >= K: #성공
            return answer
        if len(scoville) < 2 : #성공 전 더 못만듦
            return -1
        temp = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
        answer+=1
        heapq.heappush(scoville,temp)