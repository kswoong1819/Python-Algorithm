def solution(k, room_number):
    answer = []
    rooms = [0] * (k+1)
    for number in room_number:
        if rooms[number] == 0:
            rooms[number] = 1
            answer.append(number)
        else:
            find(0, k, number)
    return answer


print(solution(10, [1,3,4,1,3,1]))