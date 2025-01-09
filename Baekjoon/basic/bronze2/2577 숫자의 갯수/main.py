"""
time : 6m 53s (2트)
keyword : 수학, 구현, 사칙연산
"""

"""
<접근 방식>
1 ) 3개의 수를 받기
2) 연산 결과에서 쓰인 각 숫자들의 갯수 카운트
3) 각각 하나씩 출력

"""
a = 1
result = [0] * 10
for i in range(3) :
    b = int(input())
    a= a * b
n = list(map(int, str(a)))
for i in n :
    result[i] += 1

for i in range(10) :
    print(result[i]) 
    
    
