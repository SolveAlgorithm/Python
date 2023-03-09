def solution(cards1, cards2, goal):
    if len(cards1) > len(cards2):
        for i in goal:
            try:
                if cards1[0] == i:
                    del cards1[0]
                elif cards2[0] == i:
                    del cards2[0]
                else:
                    return "No"
            except Exception:
                return "No"
        return "Yes"
    else:
        for i in goal:
            try:
                if cards2[0] == i:
                    del cards2[0]
                elif cards1[0] == i:
                    del cards1[0]
                else:
                    return "No"
            except Exception:
                return "No"
        return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
