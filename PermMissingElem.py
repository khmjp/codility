# PermMissingElem

def solution(A):
    # write your code in Python 3.6
    comp = set(range(1, len(A)+2))
    diff = comp - set(A)
    return list(diff)[0]

A = [2, 3, 5, 4]
#A = [1]

if __name__ == '__main__':
    rs = solution(A)
    print(rs)