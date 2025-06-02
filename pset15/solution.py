def solution(Z,x,y,dx,dy):
    for t in range(10000):
        m,n = x%(2*Z), y%(2*Z)
        if (Z<m<2*Z and 0<n<Z) or (Z<n<2*Z and 0<m<Z):
            return f'Na {t} verplaatsingen bereikt Niels ({x}, {y}).'
        x+=dx
        y+=dy
    return 'Niels kan de zwarte vierkanten niet ontsnappen.'

assert solution(10,2,3,3,2) == 'Na 3 verplaatsingen bereikt Niels (11, 9).'
assert solution(18,72,6,18,6) == 'Niels kan de zwarte vierkanten niet ontsnappen.'