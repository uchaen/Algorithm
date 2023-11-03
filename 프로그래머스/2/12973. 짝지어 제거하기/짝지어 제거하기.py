def solution(s):
    stack = []
    
    for ss in s:
        if not stack:
            stack.append(ss)
        elif stack[-1] != ss:
            stack.append(ss)
        else:
            stack.pop()

    if stack: return 0
    else: return 1