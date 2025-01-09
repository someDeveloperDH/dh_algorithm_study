"""
time : 10m 32s
keyword : 수학, 구현, 사칙연산
"""

"""
<접근 방식>
c d e f g a b C

"""
music = list(map(int, input().split()))

n = music[0]

if music[0] == 1 :
    for i in range(1,8) :
        if n+1 == music[i] :
            n = n+1
            pass
        else : 
            print("mixed")
            break
    if n == 8 : 
        print("ascending")
elif music[0] == 8 :
    for i in range(1,8) :
        if n-1 == music[i] :
            n = n-1
            pass
        else : 
            print("mixed")
            break
    if n == 1 :
        print("descending")
else :
    print("mixed")
