f = open('새파일.txt','a',encoding='utf-8') # W : 읽기전용 / a: 어팬드모드
result = f.write('문서에 저장되는 내용입니다.\n')
print(result) # 사용되는 글자수가 나옴
print(len('문서에 저장되는 내용입니다.'))
f.close() # 새파일.txt 파일이 만들어짐

f = open('새파일.txt')
# for line in f.readlines():
#     print(line)

# print(f.readline())
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break

print(f.read())

f.close()