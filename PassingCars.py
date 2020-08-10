# PassingCars

def solution(A):
    # write your code in Python 3.6
    ones = [ n for n in A if n == 1 ]
    ones_num_max = len(ones)

    passing_num = 0
    ones_num = ones_num_max
    for n in A:
        if n == 1:
            ones_num -= 1
        else: # n == 0
            passing_num += ones_num
            if passing_num > 1_000_000_000:
                return -1
    return passing_num

A = [0, 1, 0, 1, 1] # return 1

if __name__ == '__main__':
    rs = solution(A)
    print(rs)