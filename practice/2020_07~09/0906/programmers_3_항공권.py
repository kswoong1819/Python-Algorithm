def solution(tickets):
    global answer
    answer = []
    used = [0] * len(tickets)
    dfs(tickets, used, ["ICN"])

    return answer

def dfs(tickets, used, visited):
    global answer
    if len(visited) == len(tickets) + 1:
        if answer != []:
            for k in range(len(visited)):
                if answer[k] < visited[k]:
                    return
                elif answer[k] == visited[k]:
                    continue
                else:
                    answer = visited.copy()
                    return
        else:
            answer = visited.copy()
        return
    for i in range(len(tickets)):
        if used[i]: continue
        if visited[-1] == tickets[i][0]:
            visited.append(tickets[i][1])
            used[i] = 1
            dfs(tickets, used, visited)
            visited.pop()
            used[i] = 0

T = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# T = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(T))