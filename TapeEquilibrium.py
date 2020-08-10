# TapeEquilibrium

def solution(A):
    # write your code in Python 3.6
    diff = {}
    A_first = A[0]
    A_second = sum(A) - A[0]
    for p in range(1,len(A)):
        diff[p] = abs(A_first - A_second)
        A_first += A[p]
        A_second -= A[p]
    return min(diff.values())

A = [3, 1] # return 1
#A = [1]

if __name__ == '__main__':
    rs = solution(A)
    print(rs)