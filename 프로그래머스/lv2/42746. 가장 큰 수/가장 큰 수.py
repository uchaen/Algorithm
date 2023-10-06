def solution(numbers):
    for i, n in enumerate(numbers):
        numbers[i] = str(n)
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int("".join(numbers)))