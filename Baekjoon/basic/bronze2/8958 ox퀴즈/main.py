"""
time : 21m 56s
keyword : 구현, 문자열
"""

"""
<접근 방식>
입력 
    테스트 케이스
    각 테스트 
출력 
    케이스 별 점수

O 누적시 + 1

"""

test_num = int(input())
answer_score = []
for i in range(test_num) :
    t_case = list(input())
    if t_case[0] == 'O' :
        answer_score.append(1)
    else :
        answer_score.append(0)
    
    add_score = 1
    for j in range(1, len(t_case)) :
        if t_case[j] == 'O' :
            if t_case[j-1] == 'O' :
                add_score += 1
                answer_score[i] += add_score
            else :
                add_score = 1
                answer_score[i] += add_score
        else : 
            pass
    
for i in range(test_num) :
    print(answer_score[i])




"""
<결과>
"""