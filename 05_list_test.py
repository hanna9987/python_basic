a = [1, 2, 3, ['a', 'b', 'c']]
print(a)
print(type(a))
print(a[0])
print(a[3][1])

a = [1, 2, 3, ['a', 'b', [1,3,5], 'c']]
print(a[3][2][1],a[3][2][2])
print(a[3][2][1:])

jumin = '000212-4111111'
print(jumin.split())

jumin = '000212 4111111'
print(jumin.split())
print(len(jumin))


a = [1, 2, 3, ['a', 'b', [1,3,5], 'c']]
print(len(a))
print(len(a[3]))

a = [1, 2, 3, ['aaaa', 'b', [1,3,5], 'c']]
print(len(a[3][0]))

a[3][0] = 'hi'
print(a)
# 리스트 수정하기(변경가능한 것만 가능)

# del a[3]
# # 리스트 삭제하기(괄호가 없음())
# print(a)
# del a
print(a)
# # nameerror: a가 없어졌다는걸 알 수 있음

a = [1, 2, 3]
a.append('qqq')
# 뒤에 들어감
print(a)
a.insert(0,'aaa') 
# 원하는 곳에 들어감 (인덱스 숫자)
print(a)
# a.sort()
# print(a)
# # 오류남. 같은 종류만 정렬가능.

a = [1, 4, 3, 2]
a.sort(reverse=True)
print(a)

a = ['a','b','c']
a.remove('b')
print(a)

a = ['a','b','b','c']
a.remove('b')
print(a)
# 맨첫번째 'b'만 제거됨

a = ['a','b','c']
print(a.pop(a.index('b')))
print(a)

t1 = (1, 2, 'a', 'b')
# del t1[0]
# # 튜플은 하나만 삭제하거나 변경 불가
print(t1[0])

