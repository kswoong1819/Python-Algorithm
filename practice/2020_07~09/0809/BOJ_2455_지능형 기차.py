import sys
sys.stdin = open('input.txt')

people = 0
max_people = 0
for i in range(4):
    down, up = map(int, input().split())
    people = people - down + up
    if max_people < people:
        max_people = people

print(max_people)