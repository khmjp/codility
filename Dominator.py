# Dominator
# 66%: performance is bad

def solution(A):
    # write your code in Python 3.6
    # make counter
    counter = {}
    first_index = {}
    for i,n in enumerate(A):
        if n not in counter.keys():
            counter[n] = A.count(n)
            first_index[n] = i

    # get dominator
    for k,v in counter.items():
        if v > len(A)//2:
            return first_index[k]
    return -1

A = [3, 4, 3, 2, 3, -1, 3, 3] # return 0 or 2 or 4 or 6 or 7
#A = []

if __name__ == '__main__':
    rs = solution(A)
    print(rs)