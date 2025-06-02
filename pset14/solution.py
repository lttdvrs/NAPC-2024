def solution(a, m, b, d, i):
    cur=a
    it,x=0,0

    while cur>=m:
        # print(f"{it+1}. current {cur} -= ({ap[x]}) {cur*ap[x]}")
        cur-=(cur*i[x])
        it+=1

        if cur<=m and b>0:
            cur+=b
            # print(f"Break has been taken, cur + {b} = {cur}, bp is now {b-d}")
            b-=d
        x=(x+1)%len(i)

    return it

assert solution(80,25,20,10,[0.1,0.3,0.4,0.1,0.2]) == 9
assert solution(100,50,0,0,[0.5,0.5,0.5,0.5,0.5]) == 2
assert solution(60,15,30,5,[0.1,0.15,0.1,0.5,0.2]) == 25
assert solution(80,70,30,10,[0.2,0.2,0.4,0.2,0.2]) == 3