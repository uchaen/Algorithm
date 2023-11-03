def solution(n):    
    nbin = [b for b in bin(n)[2:]]
    if nbin == sorted(nbin,reverse=True): #111 110 경우
        nbin.append('0')
    nbin.sort()
    for i in range(n+1,2000000):
        tmp = [b for b in bin(i)[2:]]
        tmp.sort()
        if nbin == tmp:
            return i