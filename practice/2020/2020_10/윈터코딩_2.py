def solution(encrypted_text, key, rotation):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    r = rotation % len(encrypted_text)
    text = encrypted_text[r:] + encrypted_text[:r]
    for i in range(len(key)):
        tmp = alpha.index(text[i]) - (alpha.index(key[i]) + 1)
        tmp %= 26
        answer += alpha[tmp]
    print(len(encrypted_text), len(text), len(key))
    return answer


encrypted_text = "abcdefghijklmnopqrstuvwxyz"
key = "abcdefghijklmnopqrstuvwxyz"
for i in range(1000, -1001, -1):
    rotation = i
    print(solution(encrypted_text, key, rotation))
