from Calculator import Calculator
# # Calculator 라는 모듈(파일) 안에 Calculator라는 클래스 실행행

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.__str__())
# # # print(cal1)

# cal1.add(4)
# cal1.add(5)
# cal1.add(2)

# cal2.add(9)
# cal2.sub(4)

# cal1.resultPrint()
# cal2.resultPrint()

import sys

init = input()
cal = Calculator(init)

while True:
    menu = input('''
+. 더하기  -. 빼기  *. 곱하기  /. 나누기  q. 종료
''')
    if menu == '+':
        data = input('+ ')
        cal.add(int(data))
        # cal.resultPrint()
        print(cal.result)

    elif menu == '-':
        data = input('- ')
        cal.sub(int(data))
        cal.resultPrint()

    elif menu == '*':
        data = input('* ')
        cal.mul(int(data))
        cal.resultPrint()

    elif menu == '/':
        data = input('/ ')
        cal.div(int(data))
        cal.resultPrint()

    elif menu == 'q':
        print('종료')
        sys.exit()

    else :
        print('💡 잘못 입력하셨습니다.')
        continue

#----------------------------------------
# print(Calculator.number)
# cal1 = Calculator()
# # print(cal1.result)
# print(Calculator.number)
# cal2 = Calculator()
# # print(cal2.result)
# print(Calculator.number)
# cal3 = Calculator()
# # print(cal3.result)
# print(Calculator.number)

#---------------------------------------
# from Calculator import Calculator, MoreCalculator
# import sys

# mcal = MoreCalculator()
# mcal.resultPrint()
# mcal.add(34)
# mcal.resultPrint()
# mcal.div(2)
# mcal.resultPrint()
# mcal.div(0)
# mcal.resultPrint()
# print(mcal)