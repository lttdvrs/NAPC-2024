def solution(n,s,t):
    t.sort(reverse=True)
    r = t[0]
    for i in range(1,len(t)):
        if s>=r:
            return 'Nee'
        r=min(r-s,t[i])
    return 'Ja'

assert solution(5,1, [1,2,3,4,5]) == 'Ja'
assert solution(3,2, [4,3,2]) == 'Nee'