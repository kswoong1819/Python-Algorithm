def editDistance(source, target):
    result = check(source, target, float('inf'))
    alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nxt_source = []
    nxt_target = []
    for i in range(len(source)):
        nxt_source.append(alpa.index(source[i]))
        nxt_target.append(alpa.index(target[i]))
    for j in range(1, 26):
        nxt_source = makealpa(nxt_source)
        result = check(nxt_source, nxt_target, result)

    return result

def check(sour, nxt, resul):
    s = sorted(sour)
    t = sorted(nxt)
    cnt = 0
    for i in range(len(s)):
        if cnt >= resul:
            break
        if s[i] != t[i]:
            cnt += 2
    return cnt

def makealpa(arr):
    for i in range(len(arr)):
        arr[i] = (arr[i] + 1) % 26
    return arr

source = 'ab'
target = 'ef'
print(editDistance(source, target))