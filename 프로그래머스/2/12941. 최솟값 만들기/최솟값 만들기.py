def solution(A,B):
    ans1 = 0
    ans2 = 0
    A.sort()
    B.sort()

    if len(A) < len(B):
        for idx,a in enumerate(A):
            ans1 += a * B[-idx-1]
        return ans1
    elif len(A) > len(B):
        for idx,b in enumerate(B):
            ans1 += b * A[-idx-1]
        return ans1
    else:
        for idx,a in enumerate(A):
            ans1 += a * B[-idx-1]
        for idx,b in enumerate(B):
            ans2 += b * A[-idx-1]
        return min(ans1,ans2)