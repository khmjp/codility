# Triangle

# O(n*logn)
def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    A = sorted(A)
    for i in range(2,len(A)+1):
        p = A[i-2]
        q = A[i-1]
        r = A[i]

        # ignore minus values
        if p <= 0:
            continue

        # "p < q + r" is always true
        # "q < p + r" is always true
        # check if "r < p + q" is true
        if (r - p) < q:
            return 1
    return 0

A = [10, 2, 5, 1, 8, 20] # return 60

if __name__ == '__main__':
    rs = solution(A)
    print(rs)