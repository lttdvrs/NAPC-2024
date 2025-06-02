def solution(n,w):
    w=list(map(int, w))
    a,b=0,0 
    for i in range(n):
        if w[i]==1:
            a=3
        if a > 0:
            a-=1
            b+=1
    return b

assert solution(10, '0100010100') == 8
assert solution(8, '10101010') == 8