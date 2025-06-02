def solution(s):
    return ['Imposter!', 'Groninger!']['Moi!' in s]


assert solution('Moi! Wat een lekker weertje vandaag.') == 'Groninger!'
assert solution('Geloof me, ik ben een Groninger!') == 'Imposter!'
assert solution('Ik voel me zo moi!') == 'Imposter!'