def solution(g):
    o=g.count('o')
    return f'h{'o'*(o*2)}i'

assert solution('hooooi') == 'hooooooooi'