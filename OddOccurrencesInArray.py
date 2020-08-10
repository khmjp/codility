# OddOccurrencesInArray

def solution(A):
    # write your code in Python 3.6
    odd_dict = {}
    for i, v in enumerate(A):
        if v not in odd_dict.keys():
            odd_dict[v] = i
        else:
            del odd_dict[v]
    return next(iter(odd_dict.keys()))

A = [9, 3, 9, 3, 9, 7, 9]

if __name__ == '__main__':
    solution(A)
    print(solution(A))