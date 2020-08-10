# Distinct

def solution(A):
    # write your code in Python 3.6
    return len(set(A))

A = [2, 1, 1, 2, 3, 1] # return 1

if __name__ == '__main__':
    rs = solution(A)
    print(rs)