# Flogjump
import math

def solution(X, Y, D):
    # write your code in Python 3.6
    return math.ceil((Y - X) / D)

X = 10
Y = 85
D = 30

if __name__ == '__main__':
    rs = solution(X, Y, D)
    print(rs)