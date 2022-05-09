def start_end(words):
    count = 0
    for word in words:
        if len(word) < 2:
            continue
        else:
            if word[0] == word[-1]:
                count += 1
    return count

print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))