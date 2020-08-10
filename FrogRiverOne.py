# FrogRiverOne

def solution(X, A):
    # write your code in Python 3.6
    leave = {}
    for i, p in enumerate(A):
        if p not in leave.keys():
            leave[p] = i
            if len(leave) == X:
                return i
    return -1

X = 7
A = [1, 3, 1, 7, 2, 3, 5, 4, 6, 4, 5, 9] # return 8
#A = [1]

if __name__ == '__main__':
    rs = solution(X, A)
    print(rs)