def solution(n, t):
    a, b = 0, 0
    for x in t:
        a, b = not a, not b if x == 2 else b
    return f'Lamp a is: {'Aan' if a else 'Uit'}\nLamp b is: {'Aan' if b else 'Uit'}'

assert solution(3, [1, 2, 2]) == 'Lamp a is: Aan\nLamp b is: Uit'
