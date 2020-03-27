#. while 조건이 참인 경우 하위 조건 실행

# n=5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('final number')
# print(n)


#===================================
#
# #. for문
# #. 제일 큰 숫자 찾기
#
# # a = [3,7,4,32,7,76,3,54,45]
# #
# # standard = -1
# # for n in a :
# #     if n > standard :
# #         standard = n
# #     print('현재 큰 값 :',standard, '비교 :',n)
# #
# # print('가장 큰 숫자는 :', standard)

#===================================

#. for문
#. 제일 작은 숫자 찾기

a = [7,4,32,7,76,3,54,45]
smallest = None

for n in a :
    if smallest == None :
        smallest = n
    elif n < smallest :
        smallest = n
    print('기준:',smallest, '비교값:',n)

print('가장 작은 값:' ,smallest)


#===================================

#. for문
#. 갯수 세기 & 누적 합계 구하기

# a = [3,7,4,32,7,76,3,54,45]
#
# count = 0
# sum = 0
# for n in a :
#     count = count + 1
#     sum = sum + n
# print(count)
# print(sum)



