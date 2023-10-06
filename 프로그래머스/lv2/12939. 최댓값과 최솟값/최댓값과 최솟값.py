def solution(s):
    li = s.split(" ")
    li.sort(key=lambda x: int(x))
    
    return li[0] +" "+li[-1]