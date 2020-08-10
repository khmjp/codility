def solution(A, K):
    # write your code in Python 3.6
    if len(A) != 0:
        S = K % len(A)
    else:
        S = 0
    return A[-S:] + A[:-S]

A = [1,2,3,4,5]
K = 33

if __name__ == '__main__':
    rs = solution(A, K)
    print(A)
    print(rs)