"""
time : 실패 : 20분 타임 오버 
keyword : 수학, 구현, 사칙연산
"""

"""
<접근 방식>
input :
    시도
    H(층) W(호실) N
     
첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정

n을 h로 나눴을 때 몫 +1 이 호실이 됨
                나머지가 층이된다


"""

repeat_point = int(input())
room_record = []

for i in range(repeat_point) :
    h, w ,n = map(int,input().split())
    
    if n == h*w :
        room_record.append(n)
    elif n < h : 
        room_record.append(str(n) + "01" )
    else : 
        room = (n // h) +1
        floor = n % h 

        if room < 10 :
            room_record.append(str(floor) + "0" + str(room))
        else : room_record.append(str(floor) + str(room)) 
    

for i in range(repeat_point) :
    print(int(room_record[i]))


"""
<결과>
*반례 찾는 연습 필요

"""

