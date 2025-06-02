def solution(n,d,r):
    b=2*(n+d)
    p=n+2*d
    return 'Ja' if b>=r+1 and p>=r else 'Nee'

assert solution(4,3,10) == 'Ja'
assert solution(0,2,4) == 'Nee'