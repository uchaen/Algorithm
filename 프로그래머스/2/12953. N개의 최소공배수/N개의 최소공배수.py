def solution(arr):
    def mostCommon(a,b):
        result = 1
        for i in range(max(a,b),1,-1):
            if a%i==0 and b%i==0:
                result*=i
                a, b = a//i, b//i
        return result
    
    temp = arr[0] * arr[1] // mostCommon(arr[0],arr[1])
    for i in range(2,len(arr)):
        temp = temp * arr[i] // mostCommon(temp,arr[i])
    return temp