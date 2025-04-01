# 1.계산기 만들어보기기
# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def resultPrint(self):
#         print(self.result)

#     def add(self,num):
#         self.result += num

#     def sub(self,num):
#         self.result -= num

#     def mul(self,num):
#         self.result *= num
    
#     def div(self,num):
#         self.result /= num

# 2. 디폴트값 있게 할수 있는거
class Calculator:
    def __init__(self,result):
        self.result = result
        # 인스턴스 변수 결과 첫값을 디폴트값으로 설정.
        # 초기값을 넣어야함. cal = Calculator(!), !입력.
        # result=0 이걸 넣으면 안넣으면 0인거.
    
    def resultPrint(self):
        print(self.result)

    def add(self,num):
        self.result += num

    def sub(self,num):
        self.result -= num

    def mul(self,num):
        self.result *= num
    
    def div(self,num):
        self.result /= num

# class Calculator:
#     number = 0

#     def __init__(self,result=0):
#         Calculator.number += 1
#         self.result = 0   

#     def resultPrint(self):
#         print(self.result)

#     def add(self,num):
#         self.result += num

#     def sub(self,num):
#         self.result -= num

#     def mul(self,num):
#         self.result *= num
    
#     def div(self,num):
#         self.result /= num


# class MoreCalculator(Calculator):
#     def div(self,num):
#         if num == 0:
#             print("0으로 나눌 수 없습니다.")
#         else:
#             self.result /= num
#     def __str__(self):
#         return f'성능이 향상된 계산기 결과값 {self.result} 값이 저장되어 있습니다.'