word = input()

def Palindrome(a):
    for i in range(len(a) // 2):
        if a[i] != a[-1 - i]:
            return False
        else:
            return True

print(Palindrome(word))