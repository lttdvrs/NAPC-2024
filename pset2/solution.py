def solution(n, it):
    ne=['sleutels', 'telefoon', 'laptop', 'portemonnee']
    m=[i for i in ne if i not in it]
    return 'klaar' if not m else '\n'.join(m)

assert solution(4, ['sleutels', 'telefoon', 'portemonnee', 'handschoenen']) == 'laptop'
assert solution(5, ['sleutels', 'telefoon', 'laptop', 'portemonnee', 'sjaal']) == 'klaar'
assert solution(3, ['sleutels', 'portemonnee', 'broodtrommel']) == 'telefoon\nlaptop'
