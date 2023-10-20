def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for idx,p in enumerate(prices):
        if stack and stack[-1][1] > p: #가격떨어짐
            while stack and stack[-1][1] > p:
                tmp = stack.pop()
                answer[tmp[0]] = idx - tmp[0]
        stack.append([idx,p])

    for s in stack: #끝까지 가격 안떨어짐
        answer[s[0]] = len(prices) - s[0] - 1
    return answer