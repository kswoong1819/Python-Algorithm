def push(item):
    a.append(item)

def pop():
    if len(a) == 0:
        return
    else:
        return a.pop(-1)

a = []
print(a)
push('D4 까지 풀기')
print(a)
push('진실이 공부시키기')
print(a)
push('IM pass')
print(a)
pop()
print(a)
pop()
print(a)
pop()
print(a)