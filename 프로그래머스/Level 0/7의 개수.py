def solution(array):
    num = 0
    for i in array:
        while i % 10 > 1:
            if i % 10 == 7:
                num += 1
            i = i // 10
        if i == 7:
            num += 1
            continue
    return num


print(solution([7, 77, 17]))
