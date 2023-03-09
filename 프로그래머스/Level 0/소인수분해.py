def solution(n):
    lists = []
    for i in range(2, n+1):
        if n % i == 0:
            lists.append(i)
            while n % i == 0:
                n = n / i
        elif n == 0:
            break
    return lists

print(solution(42000))
