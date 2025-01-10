"""
time : 21m 30s
keyword : 구현, 문자열
"""

"""
<접근 방식>
입력 :
    단어
출력
    a ~ z
    처음 등장하는 위치를
    포함되어 있지 않은 경우에는 -1을 출력
    공백으로 구분

"""
word = list(input())
alp = {'a' : -1, 'b' : -1, 'c' : -1 , 'd' : -1, 'e' : -1, 'f' : -1, 'g' : -1, 
        'h' : -1, 'i' : -1, 'j' : -1, 'k' : -1, 'l' : -1, 'm': -1 , 'n' : -1, 
        'o' : -1, 'p' : -1, 'q' : -1, 'r' : -1, 's' : -1, 't': -1, 'u' : -1,
        'v' : -1, 'w': -1, 'x' : -1 , 'y': -1, 'z': -1}

for i in range(len(word)) :
    if alp[word[i]] == -1 :
         alp[word[i]]  = i
    else :
        pass


print(' '.join(map(str,alp.values())))







"""
<결과>


"""