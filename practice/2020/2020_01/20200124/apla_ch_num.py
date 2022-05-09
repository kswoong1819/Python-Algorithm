word = input()

for alpa in word:
    alpa_num = ord(alpa) - 64
    print(alpa_num, end=' ')