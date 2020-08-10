def solution(N):
    # write your code in Python 3.6
    bi = bin(N)[2:]
    zeros = bi.strip('0').split('1')
    zero_len = [len(z) for z in zeros]
    return max(zero_len)

N = 1101

if __name__ == '__main__':
    solution(N)