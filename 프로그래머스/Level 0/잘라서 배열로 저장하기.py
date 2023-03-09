def solution(my_str, n):
    num = len(my_str) / n
    if len(my_str) % n != 0:
        num = int(num) + 1
    else:
        num = int(num)
    lists = [my_str[0:n]]
    for i in range(1, num):
        lists.append(my_str[n * i:(i+1)*n])
    return lists


print(solution("abcdef123", 3))
