def solution(n,a):
    a.sort()
    return sum(a[:2])

assert solution(3, [4,9,5]) == 9
assert solution(10, [49,75,18,96,94,43,46,76,90,87]) == 61

