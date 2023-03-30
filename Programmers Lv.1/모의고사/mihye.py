def solution(answers):
    answer = []

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    anum = 0
    bnum = 0
    cnum = 0

    i = 0

    for x in answers:
        if a[i % len(a)] == x:
            anum += 1
        if b[i % len(b)] == x:
            bnum += 1
        if c[i % len(c)] == x:
            cnum += 1
        i += 1

    m = max(anum, bnum, cnum)
    if m == anum:
        answer.append(1)
    if m == bnum:
        answer.append(2)
    if m == cnum:
        answer.append(3)

    return answer