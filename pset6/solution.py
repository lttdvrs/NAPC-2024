def solution(hw1, hw2, hw3, midterm, final):
    g = [hw1,hw2,hw3]
    hw = sum(sorted(g)[-2:])/2 * 0.3
    m = midterm*0.2
    e = final*0.5
    return hw+m+e

assert solution(8.5, 4.1, 8.9, 9.2, 10) == 9.45
assert solution(8.4, 9.0, 7.2, 6.8, 5.9) == 6.92 
assert solution(7.8638630327, 1.8464076124, 7.3171138581, 5.8339423655, 7.3380136884) == 7.11294185092
