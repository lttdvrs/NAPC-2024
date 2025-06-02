def solution(n, k, guesses):
    first,second,*xs = list(set([(abs(x - k), x) for x in guesses]))
    for x in xs:first,second, _ = sorted((first, second, x))
    return second[1]

assert solution(3, 10, [7, 15, 12]) == 7
assert solution(5, 20, [17, 17, 15, 23, 50]) == 23
assert solution(7, 16360, [50843, 82492, 6468, 98519, 14206, 49461, 50061]) == 6468

