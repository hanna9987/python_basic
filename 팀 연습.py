# 주민등록 번호를 입력받아서 다음을 출력해 줍니다. 
# 성별(남자,여자)
# 생년월일(00년 1월 1일생)
# 뒷자리 숫자를 첫글자는 그대로 나머지는 *로 변경해서 출력
# 입력시 글자 앞, 위로 공백이 포함될 수 있습니다. (공백처리)

# input()을 이용하여 주민등록을 입력 받음.
# 입력값은 '000000-0000000' 형태로 작성하여야 함.
# '0'에는 숫자만 사용 가능.
# '-' 바로 다음 값은 '1,2,3,4'만 가능.
# 받은 값은 number 이름의 변수로 저장.
# number에 저장되어 있는 값에서 indext()를 이용하여 '-'의 위치 확인.
# 확인된 위치 다음 값을 gender 이름의 변수로 저장.
# gender에 저장되어 있는 값에서 '1,3'이면 남자, '2,4'면 여자로 출력


# 이메일 주소는 최소 5글자를 넘어야 됩니다.
# 최대 20글자까지 가능합니다.
# 반드시 글자 중간에 '@' 문자가 포함되어야 합니다.
# input()을 이용하여 입력 받습니다.
# 받은 값은 email 이름의 변수에 저장됩니다.
# email에 저장되어 있는 값에서 indext()를 이용하여 @의 위치를 확인합니다.
# 찾은 위치값은 index라는 이름으로 저장합니다.
# email의 값에서 처음부터 index에 저장되어 있는 값까지 슬라이싱 합니다.
# 스라이싱 한 값을 data 변수에 저장합니다.
# 변수값을 pirnt()를 이용해서 출력합니다.

# 123456-2345678
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