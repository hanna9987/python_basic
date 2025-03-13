# 계산기를 만든다 > 사칙연산 필요
def add(a,b):
    return a + b 

def sub(a,b):
    print(a - b)
    # return a - b 없이 그냥 바로 실행, 그럼 출력값만 남고 값을 받아 사용할 수 없음
    # sub(3,1)
    print('결과는 ', a - b) #값여러개 넣어도 가능.

def mul(a,b):
    return a * b

def indata():
    a = int(input('숫자를 입력하세요 >> '))
    return a

# def add_many(*args): # *매개변수: 입력값이 몇개가 될지 모를때
#     print(type(args)) #class 'tuple' 값이 변경 불가능함.
#     for i in args:

# # result = add(1,3)
# # print(result)


# # data1 = indata()
# # data2 = indata()
# # sub(data1, data2) 

# # add_many(1,2,3,4,5,6,7,8,9)

# def add_many(*args):
#     print(type(args))
#     result = 0
#     for i in args:
#         result += i
#     return result
# print(add_many(1,2,3,4,5,6,7,8,9))


def add_many(*args,mode='k'): #뒤쪽에 값은 보통 디폴트값(기본값)으로 값을 정해 넣음.
    print(type(args)) #class 'tuple' 값이 변경 불가능함.
    result = 0
    for i in args:
        result += i
    return result
print(add_many(1,2,3,4,5,6,7,8,9))
print(add_many(1,2,3,4,5,6,7,mode='yy'))

def item_print(**items):
    print(type(items))
    print(items)

item_print(a='hong', b=22)


a1 = 0
def add(a,b):
    print(a1)
    return a + b
add(1,2)