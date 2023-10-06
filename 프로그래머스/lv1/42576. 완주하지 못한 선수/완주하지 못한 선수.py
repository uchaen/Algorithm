def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for idx,c in enumerate(completion):
        if participant[idx] != c:
            return participant[idx]
    return participant[-1]