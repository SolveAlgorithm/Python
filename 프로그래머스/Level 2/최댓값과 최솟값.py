def solution(s):
    lists = list(map(int, s.split()))
    return str(min(lists)) + " " + str(max(lists))
