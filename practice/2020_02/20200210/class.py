# a = '안녕하세요'
# b = "I'm iron man"
# c = '"임동규 선수를 트레이드 하겠습니다"라고 백승수 단장이 말했다'
# d = '''나는
# IM을
# 딸 수 있다.'''
# e =  '허리' + '피라우'
# f = '껄'*3
#
# print(d)

# a = '1q2w3e4r'
# b = '123123a'
# c = '1aaa23'
# d = 'Asdf1234'
# password = [a,b,c,d]
#
# for j in password:
#     cnt_digit = 0
#     cnt_alpha = 0
#     for i in range(len(j)):
#         if a[i].isdigit():
#             cnt_digit += 1
#         if a[i].isalpha():
#             cnt_alpha += 1
#
#     if cnt_digit >= 3 and cnt_alpha >= 4:
#         print('True')
#     else:
#         print('False')

# word = '삼성청년소프트웨어아카데미'
# words = list(word)
#
#
# for i in range(len(word)):
#     print(word[-1-i],end='')
# print()
#
# words.reverse()
# print(''.join(words))

word1 = 'A pattern matching algorithm'
word2 = 'rithm'
# word1 = list(word_1)
# word2 = list(word_2)


cnt = 0
for i in range(len(word1)):
    cnt += 1
    if word1[i] == word2[0]:
        for j in range(i, i+len(word2)+1):
            if i != word1[j]:
                print('없넹')
                break
        else:
            print(cnt)
            break

