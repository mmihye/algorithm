def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    print(citations)

    for n in citations:
        if n >= citations.index(n) + 1:
            answer = citations.index(n) + 1

    return answer