"""
time : 3m 46s
keyword : 구현, 문자열
"""

"""
<접근 방식>
문자열에는 몇 개의 단어가 있을까? 

기준 : 공백
1 2 3 = 공백 2 단어 3
"""

a = input()
b = a.split()
print(len(b))