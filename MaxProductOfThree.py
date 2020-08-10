# MaxProductOfThree

# O(n*logn)
def solution(A):
    # write your code in Python 3.6
    sortA = sorted(A)
    ans_ppp = sortA[-3] * sortA[-2] * sortA[-1]
    ans_mmp = sortA[0] * sortA[1] * sortA[-1]
    if ans_ppp < ans_mmp:
        return ans_mmp
    else:
        return ans_ppp

A = [-3, 1, 2, -2, 5, 6] # return 60

if __name__ == '__main__':
    rs = solution(A)
    print(rs)