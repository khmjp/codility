# PermCheck

def solution(A):
    # write your code in Python 3.6
    setA = set(A)
    setComp = set(range(1,len(A)+1))
    if setA == setComp:
        val = 1
    else:
        val = 0
    return val

#A = [4, 1, 3, 2] # return 1
#A = [1] # 1
#A = [1, 1] # 0
A = [2, 2] # 0

if __name__ == '__main__':
    rs = solution(A)
    print(rs)