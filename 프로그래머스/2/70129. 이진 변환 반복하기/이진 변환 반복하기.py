from collections import Counter

def solution(s):
    count = 0
    zero = 0
    while s!="1":        
        c = Counter(s) #O(n)
        zero += c['0']

        s = format(c['1'], 'b')        
        count += 1        
    
    return [count, zero]