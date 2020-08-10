# Brackets

def solution(S):
    # write your code in Python 3.6
    matches = {
        "{": "}",
        "[": "]",
        "(": ")",
    }
    stack = []

    for l in S:
        if l in matches.keys():
            stack.append(l)
        elif l in matches.values():
            if len(stack) != 0 and matches[stack[-1]] == l:
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


#A = '{[()()]}' # return 1
A = "([)()]"   # return 0

if __name__ == '__main__':
    rs = solution(A)
    print(rs)