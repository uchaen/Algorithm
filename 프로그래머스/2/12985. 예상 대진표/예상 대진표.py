def solution(n,a,b):
    a-=1
    b-=1
    for i in range(1,21):
        a = a//2
        b = b//2
        if a==b:
            return i