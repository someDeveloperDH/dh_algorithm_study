"""
time : 12m 53s
keyword : 수학, 구현, 사칙연산
"""

"""
<접근 방식>
첫째 줄에 테스트 케이스의 개수 T

각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 (1~20)

각 문자를 R번 반복해 새 문자열 P

1 ) 문자열 분리
2) R번 만큼 복사
3) 문자열 이어서 출력

"""

num = int(input())
result = []


for i in range(num) :
    n, sentence = map(str, input().split())
    n = int(n)
    a = list(sentence)
    for j in range(len(a)) :
        b = a[j]
        a[j] = b*n
    result.append("".join(a))

for i in result :
    print(i)
        
        
    
    
    
