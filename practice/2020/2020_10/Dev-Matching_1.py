def solution(votes, k):
    answer = ''
    vote = {}
    for car in votes:
        if car in vote:
            vote[car] += 1
        else:
            vote[car] = 1
    vote = sorted(vote.items())
    vote = sorted(vote, key=lambda x: x[1], reverse=True)
    max_vote = 0
    out_vote = 0
    for i in range(k):
        max_vote += vote[i][1]
    for j in range(len(vote) - 1, -1, -1):
        out_vote += vote[j][1]
        if out_vote >= max_vote:
            answer = vote[j + 1][0]
            break
    return answer


votes = ["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER",
         "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"]
k = 2
print(solution(votes, k))
