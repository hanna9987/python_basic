# dic 공부
name_card = {'name':'홍길동', 'tel':'010-888-9999', 'address':'부산', 'email':'han@mail.net'} 
#엔터로 줄바꿈 오류가능성 o/ 하지만 ',' 뒤에는 사용해도 문제 없음
name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'han@mail.net',
             'tel':'010-9987'}
# 뒤에 있는 키값 덮어씀(중복되면 뒤에 값만 인정)

print(name_card)

name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'han@mail.net',
             '1.1':'010-9987'} #실수값은 키값으로 안쓰는게 좋음
print(name_card)

# # name_card = {'name':'홍길동',
#              'tel':'010-888-9999',
#              'address':'부산',
#              'email':'han@mail.net',
#               [1.1]:'010-9987'} #리스트는 키값 불가능> 변할수 있으니, 튜플은 가능하지만 잘 안씀
# # print(name_card)

name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'han@mail.net'}

name_card['etc'] = '이사갈수도..'
print(name_card)

name_card['etc'] = ['이사갈수도..','1년안에']
print(name_card)
print(name_card['address'])
print(name_card['etc'][1])

del name_card['address']
print(name_card)

print(type(name_card))

print(len(name_card)) #len 내용 갯수 ',' 기준임.

# print(name_card['address']) 삭제했으니 오류가 남.

print('address' in name_card) #없어서 false 나옴

print('address' not in name_card) #없으니 true 나옴

print(name_card.keys())

print(list(name_card.keys()))
print(name_card.values())
print(name_card.items()) #키밸류를 튜플로 묶어 보여줌.

for k in name_card: #한쌍씩 나오도록 보고싶을때
    print(k) #키라고 안했는데 for문에서는 키만 나옴 보통
    print('-'*30)

for k in name_card.keys():
    print(k)
print('-'*30)

for k in name_card.values():
    print(k)
print('-'*30)

for k in name_card.items():
    print(k)
print('-'*30)

for k,v in name_card.items():
    print(k,v) #튜플 없이 되네? 왜지?

name_card.clear()
print(name_card)

print(name_card.get('address')) #값이 없는데 오류가 아닌 none이 리턴.

# set 배우기
s1 = set([1,2,3,3,2])
print(s1)

s2 = set('hello')
print(s2)

s1 = set(1,2,3,3,2)
print(s1)