'''
<1330번 두 수 비교하기>
걸린시간 : 1m 46s


'''
# a, b = map(int,input().split())

# if a < b : 
#     print("<")
# elif a > b :
#     print(">")
# else :
#     print("==")


'''
<2438 별찍기>
time : 2m 45s



''' 

# n = input()
# n = int(n)

# for i in range(n) :
#     print("*" * (i+1))

   
'''
<2475 검증수>
time : 8m 34s
키워드 : 수학,구현, 사칙연산


5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

파이썬 기본 문법.
'''

# a, b, c, d, e = map(int, input().split())
# print(((a**2) + (b**2) + (c**2) + (d**2)+ (e**2))%10)


'''
<2739 구구단>
time : 1m 32s
키워드 : 수학, 구현


'''
# n = input()
# n = int(n)

# for i in range(1,10) :
#     print(f"{n} * {i} = {n*i}")

'''
<2741 N찍기>
time : 2m 5s
키워드 : 구현


런타임 에러?
'''
# n = input()
# n = int(n)

# for i in range(1, n+1) :
#     print(i)


'''
<2753 윤년>
time : 5m 45s
키워드 : 수학, 구현, 사칙연산

input : 연도
output : 1 or 1
 1)  4의 배수이면서, 100의 배수가 아닐 때
 2) 400의 배수일 때
 
'''



# n = input()
# n = int(n)


# if (n%4 == 0 and n%100 != 0) or (n%400 == 0) :
#     print("1")
# else : 
#     print("0")


'''
<9498 시험 성적>
time : 6m 5s
keyword : 구현

 90 ~ 100점은 A, 
 80 ~ 89점은 B, 
 70 ~ 79점은 C, 
 60 ~ 69점은 D, 
 나머지 점수는 F
'''

# n = input()
# n = int(n)

# remain = n//10

# if remain >= 9 : print("A")
# elif  remain == 8 : print("B")
# elif  remain == 7 : print("C")
# elif  remain == 6 : print("D")
# else : print("F")

'''
<10171 고양이>
'''

# print(
# """\\    /\\
#  )  ( ')
# (  /  )
#  \\(__)|
# """)


'''
<10172 개>

'''

# print("""|\\_/|
# |q p|   /}
# ( 0 )\"\"\"\\
# |"^"`    |
# ||_/=\\\\__|      
# """   
# )

'''
[10871 X보다 작은 수]
time : 14m 50s
keyword : 구현

첫 줄 A와 X 
A에서 X보다 작은 수 전부 출력

'''

# n , x = map(int,input().split())
# a = list(map(int, input().split()))
# answer = []
# for i in range(n) :
#     if a[i] < x :
#         answer.append(a[i])
# result = ' '.join(map(str, answer))
# print(result)
     
'''
[10950 A+B -3]
time : 3m 26s
keyword : 구현

'''
# n = input()
# n = int(n)
# answer = []

# for i in range(n) :
#     a, b = map(int, input().split())
#     answer.append(a+b)

# for i in range(n) :
#     print(answer[i])    





'''
[10951 A+B -4]
time : 
keyword : 구현, EOF

'''
# while True:

#   try:

#      a,b=map(int,input().split())

#      print(a+b)

#   except:

#      break

'''
[10952 A+B -5]
time : 1m 53s
keyword : 구현

'''

# while True:

#   try:

#      a,b=map(int,input().split())
     
#      if a == 0 and b == 0 :
#          break
#      print(a+b)

#   except:

#      break

'''
[11654 아스키코드 ]
time : 1m 25s
keyword : 구현

'''
# a = input()
# print(ord(a))


'''
[25083 새싹]
time : 
keyword : 구현

'''
# print("""         ,r'"7
# r`-_   ,'  ,/
#  \\. ". L_r'
#    `~\\/
#       |
#       |"""
# )


'''
[25083 새싹]
time : 2m 8s 
keyword : 구현, 문자열

'''

# word = input()
# idx = input()
# idx = int(idx)

# print(word[idx-1])

'''

[2439 별 찍기-2] - 브론즈 4
time : 9m 13s 
keyword : 구현

'''
# n = input()
# n =int(n)
# a = ' '
# b = '*'
# for i in range(n) :
#     c = (a * (n-(i+1))) + (b * (i+1))
#     print(c)
    
'''
[2884 알람 시계] - 브론즈 3
time : 해결
keyword : 구현

* 첫째 줄에 두 정수 H와 M이 주어진다.
    (0 ≤ H ≤ 23, 0 ≤ M ≤ 59
    0:0(자정)
    23:59(다음날 자정 1분 전)

'''

h, m =map(int, input().split())

m = m - 45

if m < 0 :
    m = 60 + m
    if h != 0 :
        h -= 1
    else : h = 23

    
print(f"{h} {m}")