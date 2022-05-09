def solution(info, query):
    answer = []
    I = len(info)
    Q = len(query)
    info2 = []
    for i in range(I):
        info2.append(info[i].split())
    query2 = []
    for i in range(Q):
        tmp = []
        for check in query[i].split():
            if check != 'and':
                tmp.append(check)
        query2.append(tmp)

    for word in query2:
        cnt = 0
        for i in range(I):
            for j in range(4):
                if word[j] == '-':
                    continue
                if info2[i][j] != word[j]:
                    break
            else:
                if int(info2[i][4]) >= int(word[4]):
                    cnt += 1
        answer.append(cnt)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
