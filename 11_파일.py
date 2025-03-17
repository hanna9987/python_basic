# f = open('새파일.txt','a',encoding='utf-8') # W : 읽기전용 / a: 어팬드모드
# result = f.write('문서에 저장되는 내용입니다.\n')
# print(result) # 사용되는 글자수가 나옴
# print(len('문서에 저장되는 내용입니다.'))
# f.close() # 새파일.txt 파일이 만들어짐

# f = open('새파일.txt')
# for line in f.readlines():
#     print(line)

# print(f.readline())
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break

# print(f.read())

# f.close()

# ----------------------------------
# #json 파일 배우기
import json

data = {'name':'홍길동','age':22}
with open('myinfo.json', 'w') as f:
    json.dump(data,f,indent=2,ensure_ascii=False) #indent 들여쓰기기

with open('myinfo.json') as f: #'w' 안쓰면 기본 'r'모드
    data = json.load(f) #loads/load 차이는 파일자체 그대로 사용하면 단수명 씀

print(type(data))
print(data)

#--------------------------------------
#피클 배우기
import pickle

data = {'name':'홍길동','age':22}
with open('myinfo.pickle', 'wb') as f: #제이쓴은 텍스트기반 피클은 그대로 저장? 그래서 바이너리형태라서 w만이아니라 wb라고 씀씀
    pickle.dump(data,f)

with open('myinfo.pickle','rb') as f: #'w' 안쓰면 기본 'r'모드
    data = pickle.load(f) #들여쓰기,아스키 지원 안됨

print(type(data))
print(data)