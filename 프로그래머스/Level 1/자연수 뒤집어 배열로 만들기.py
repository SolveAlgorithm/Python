def solution(n):
    n_list = []
    while n / 10 != 0:
        n_list.append(n % 10)
        n = n // 10
    return n_list


solution(12345)
