"""
time : 5m 9s
keyword : 수학, 사칙연산
"""

"""
<접근 방식>
10개를 한줄씩 입력
42로 나눈 나머지들
나머지들 중복 제거 후, 갯수 출력



"""
target_num = 42
target_list = []

for i in range(10) : 
    n = int(input())
    target_list.append(n %42)

print(len(set(target_list)))
    





"""
<결과>


"""