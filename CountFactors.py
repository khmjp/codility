# CountFactors

def solution(N):
    # write your code in Python 3.6
    import math
    sqrt = math.sqrt(N)
    cnt = 0
    for i in range(1, int(sqrt)+1):
        if N % i == 0:
            cnt +=2

    if int(sqrt) == sqrt:
        cnt -= 1

    return cnt

N = 24 # return 8

if __name__ == '__main__':
    rs = solution(N)
    print(rs)