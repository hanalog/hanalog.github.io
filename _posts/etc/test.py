def solution(maxSize, actions):
    from collections import deque
    back, forward = deque(), deque()
    answer = deque(maxlen=maxSize)
    cur = "start"
    for action in actions:
        if action == "B":
            if back:
                forward.append(cur)
                cur = back.pop()
                answer.appendleft(cur)
        elif action == "F":
            if forward:
                back.append(cur)
                cur = forward.pop()
                answer.appendleft(cur)
        else:
            forward = deque()
            back.append(cur)
            cur = action
    return answer

print(solution(3, ["1", "2", "3", "4", "5"]))