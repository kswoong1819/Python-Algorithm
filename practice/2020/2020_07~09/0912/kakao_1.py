def solution(new_id):
    id = new_id.lower()
    id2 = ''
    for k in range(len(id)):
        if id[k].isalpha() or id[k].isnumeric() or id[k] == '-' or id[k] == '_' or id[k] == '.':
            if len(id2) != 0 and id[k] == '.' and id2[-1] == '.':
                continue
            if len(id2) == 0 and id[k] == '.':
                continue
            id2 += id[k]
    if len(id2) == 0:
        id2 = 'a'
    if id2[-1] == '.':
        id2 = id2[:-1]
    if len(id2) >= 16:
        id2 = id2[:15]
        if id2[-1] == '.':
            id2 = id2[:-1]
    if len(id2) <= 2:
        while len(id2) < 3:
            id2 += id2[-1]

    return id2


# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
new_id = "abcdefghijklmn.p"

solution(new_id)
