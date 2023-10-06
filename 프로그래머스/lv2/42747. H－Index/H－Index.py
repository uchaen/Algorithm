def solution(citations):
    cit = sorted(citations, reverse=True)
    for idx,c in enumerate(cit):
        if c < idx+1:
            return idx
    return len(cit) #[5,5,5,5]인경우 h=4