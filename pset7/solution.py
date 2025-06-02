def solution(a,b):
    m=0
    for x in range(len(a)):
        if a[x]==b[x]: 
            m+=1
    return f'{m}/{len(a)}'

assert solution('MGINTRELFLNFTIVLITVILMWLLVRSYQY', 'MERSTQELFINFTVVLITVLLMWLLVRSYQY') == '24/31'
