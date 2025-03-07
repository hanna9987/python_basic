# 이메일 주소를 입력받습니다. 입력시 ***@** 형태입니다.
# 입력받아서 아이디만 출력해 주세요.

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

email = input('메일 주소를 입력하세요 >>> ')
print('값은 5~20 범위에서 ',len(email))
print('값은 1이 나와야 됨',email.count('@'))
index = email.index('@')
data = email[:index]
print(data)

# 주민등록 번호를 입력받아서 다음을 출력해 줍니다. 
# 성별(남자,여자)
# 생년월일(00년 1월 1일생)
# 뒷자리 숫자를 첫글자는 그대로 나머지는 *로 변경해서 출력
# 입력시 글자 앞, 위로 공백이 포함될 수 있습니다. (공백처리)