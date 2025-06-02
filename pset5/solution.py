import math
def solution(r):
    return f'De oppervlakte is: {math.pi*(r**2):.2f}'

assert solution(6) == 'De oppervlakte is: 113.10'
assert solution(4) == 'De oppervlakte is: 50.27'