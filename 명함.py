ntn = int(input("사람수를 입력하시오"))

while ntn != 0:
    if ntn > 4:
         name1 = input("이름을 입력하시오=")

         number1 = input("번호를 입력하시오=")

         email1 = input("이메일을 입력하시오=")

         job1 = input("직업을 입력하시오=")

         group1 = input("부서를 입력하시오=")

         print("----------------------------------------------------------------------------")

         print(("이름:")+   (name1))

         print(("번호:")+ (number1))

         print(("직업:")+    (job1))

         print(("부서:")+  (group1))

         print(("이메일:")+(email1))

         print("----------------------------------------------------------------------------")

         first = [(name1), (number1), (job1), (group1), (email1)]
         ntn = (ntn - 1)
     
    elif ntn > 3:
         
         name2 = input("이름을 입력하시오=")

         number2 = input("번호를 입력하시오=")

         email2 = input("이메일을 입력하시오=")

         job2 = input("직업을 입력하시오=")

         group2 = input("부서를 입력하시오=")

         print("----------------------------------------------------------------------------")

         print(("이름:")+   (name2))

         print(("번호:")+ (number2))

         print(("직업:")+    (job2))

         print(("부서:")+  (group2))

         print(("이메일:")+(email2))

         print("----------------------------------------------------------------------------")

         second = [(name2), (number2), (job2), (group2), (email2)]

         ntn = (ntn - 1)

    elif ntn > 2:
         
         name3 = input("이름을 입력하시오=")

         number3 = input("번호를 입력하시오=")

         email3 = input("이메일을 입력하시오=")

         job3 = input("직업을 입력하시오=")

         group3 = input("부서를 입력하시오=")

         print("----------------------------------------------------------------------------")

         print(("이름:")+   (name3))

         print(("번호:")+ (number3))

         print(("직업:")+    (job3))

         print(("부서:")+  (group3))

         print(("이메일:")+(email3))

         print("----------------------------------------------------------------------------")

         third = [(name3), (number3), (job3), (group3), (email3)]

         ntn = (ntn - 1)

    elif ntn > 1:
         
         name4 = input("이름을 입력하시오=")

         number4 = input("번호를 입력하시오=")

         email4 = input("이메일을 입력하시오=")

         job4 = input("직업을 입력하시오=")

         group4 = input("부서를 입력하시오=")

         print("----------------------------------------------------------------------------")

         print(("이름:")+   (name4))

         print(("번호:")+ (number4))

         print(("직업:")+    (job4))

         print(("부서:")+  (group4))

         print(("이메일:")+(email4))

         print("----------------------------------------------------------------------------")

         forth = [(name4), (number4), (job4), (group4), (email4)]

         ntn = (ntn - 1)

    elif ntn > 0:
         
         name5 = input("이름을 입력하시오=")

         number5 = input("번호를 입력하시오=")

         email5 = input("이메일을 입력하시오=")

         job5 = input("직업을 입력하시오=")

         group5 = input("부서를 입력하시오=")

         print("----------------------------------------------------------------------------")

         print(("이름:")+   (name5))

         print(("번호:")+ (number5))

         print(("직업:")+    (job5))

         print(("부서:")+  (group5))

         print(("이메일:")+(email5))

         print("----------------------------------------------------------------------------")

         fifth = [(name5), (number5), (job5), (group5), (email5)]

         ntn = (ntn - 1)

         list = print((first),(second),(third),(forth),(fifth),sep='\n')
