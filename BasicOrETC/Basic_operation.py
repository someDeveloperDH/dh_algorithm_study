'''
[1000번 A+B]

<수도>
input : 두개의 정수 
output : 입력 받은 두개의 정수 더하기

한줄에서 A, B 를 입력 받기 -> map, input, split
A+B 형태로 출력

'''
'''

걸린 시간 : 1분 47초
pypy3
메모리 : 108384
시간 : 96 
코드길이 : 57
성공 

Python3
메모리 : 32412
시간 : 36
코드길이 57
성공
'''

# num1, num2 = map(int, input().split())

# print(num1 + num2)

###다른 사람 풀이
## Python 31120 /36/28 
'''
코드 설명 :
    sum(*open(0,"rb"))%23
    open
    

내 코드와 비교 : 
    1. 스펙
        *메모리 측면에서 

배운점 :
    1. PyPy3인가 Python3인가에 따라서 메모리 시간 차이가 심하다. Python3가 더 좋은 듯하다 --> 왜지? 
    2. 계정에 따라서 스펙 성능에 약간의 차이가 존재 --> 왜 일까?
    3. 
'''
# print(sum(*open(0,"rb"))%23)



##################################################

'''
[1001번 A-B]

'''
# num1, num2 = map(int, input().split())

# print(num1 - num2)

'''
[1008 A/B]

'''
# num1, num2 = map(int, input().split())
# print(num1 / num2)



'''
[10869 사칙연산]
관련 : [10998 A*B]
time : 2m
keyword : 수학, 구현, 사칙연산

A+B, A-B, A*B, A/B(몫), A%B
'''
# a, b = map(int, input().split())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

'''
[11720 숫자의 합]
time : 5m 13s 
keyword : 수학

<분석>
첫째 줄에 숫자의 개수 N
둘째 줄에 숫자 N개가 공백없이
숫자 N개의 합 출력
'''

# n = input()
# a = input()
# a_list = list(a)
# result = 0

# for i in range(len(a_list)) :
#     result += int(a_list[i])

# print(result)

'''
[11720 숫자의 합] - 브론즈 4
time :  5m 39s
keyword : 수학



'''
# a = input()
# b = input()
# c = input()

# str_result = int(a + b) - int(c)
# int_result = int(a) + int(b) - int(c)



# print(int_result)
# print(str_result)

'''
[36+3 최댓 값] - 브론즈 3
time :  
keyword : 수학, 구현


첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수

첫째 줄에 최댓값을 출력
둘째 줄에 최댓값이 몇 번째 수
'''


max_num = 0
idx = 0

for i in range(9) : 
    a = input()
    a =int(a)
    
    if a > max_num :
        max_num = a
        idx = i+1
   

print(max_num)
print(idx)