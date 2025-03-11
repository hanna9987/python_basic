
# 1. 주민번호 등록

# 주민등록번호는 "******-*******"의 형식으로 입력
# input()으로 "주민등록번호를 입력하세요 >>>" 프롬프트 입력 후 받은 값은 number 변수로 저장
# number 값을 .strip() 로 공백 처리
# 하이픈이 없으면 오류 -> print('값 1인지 확인', number.count('-'))


# 2. 성별 확인

# 인덱스7 값을 도출하여 gender 변수로 저장.
# gender 변수값을 int를 사용하여 숫자로 변환.
# print("남자는 '1', 여자는 '0' >>>", gender_int % 2)로 출력


# 3. 생년월일 

# number[:6]로 생년월일 슬라이싱하여 birth_data 이름으로 변수 저장
# 생년월일 추출 (number[:6]에서 년, 월, 일 구하기)
# 주민등록번호 앞 6자리 (년, 월, 일)을 넣어 생년월일 출력하기 
# birth_data = number[:6] 
# a = birth_data[:2] 
# b = birth_data[2:4] 
# c = birth_data[4:6]
# print(birth_date = f"{a}년 {b}월 {c}일생")로 출력


# 4. 뒷자리 * 변경

# *로 변경할 뒷자리 정보를 back 변수로 저장한다 
# back  = number[8:]
# print(back) 해서 값을 찍어보고 도출되는 주민번호 뒤 6자는 *표 처리
# *표 처리는 replace 메소드를 사용해서 변경하고 도출되는 값은 masked라는 변수로 저장
# masked = number.replace(back, ‘******’)
# 변수 masked 값을 print()를 이용하여 출력한다 -> print(masked)



# 예시) 123456-2345678
number = input('주민등록번호를 입력하세요 >>> ')
number.strip()
print(number.count('-'))
gender = number[7]
print(gender)
gender_int = int(gender)
print("남자는 '1', 여자는 '0' >>>", gender_int % 2)
birth_data = number[:6]
print(birth_data)
a = birth_data[:2] 
b = birth_data[2:4] 
c = birth_data[4:6]
birth = f"{a}년 {b}월 {c}일생"
print(birth)
back = number[8:]
print(back)
masked = number.replace(back, '*******')
print(masked)