def solution(user_id, banned_id):
    answer = 0
    same_list = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                if check_word(banned_id[i], user_id[j]):
                    same_list[i].append(user_id[j])




    return answer


def check_word(word1, word2):
    for i in range(len(word1)):
        if word1[i] == '*':
            continue
        if word1[i] != word2[i]:
            return 0
    return 1

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))