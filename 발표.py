import sys

display = '''
--------------------------------------------------------------
1.명함입력, 2.명함수정, 3.명함삭제, 4.명함목록보기, 5.종료
--------------------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ''
cards = []
while True:
    menu = input(display)
    if menu == '1':
        print('명함입력')
    elif menu == '2':
        print('명함수정')
    elif menu == '3':
        print('명함삭제')
    elif menu == '4':
        print('명함목록보기')
    elif menu == '5':
        print('프로그램 종료')
        sys.exit()
    else:
        print('메뉴선택을 잘못하셨습니다.')

    # 1번 선택: 명함 입력
    if choice == '1':
        print("\n[ 명함 입력 ]")
        name = input("이름을 입력해주세요: ")
        email = input("이메일을 입력해주세요: ")
        phone = input("전화번호를 입력해주세요: ")
        affiliation = input("소속(학교/직장)을 입력해주세요: ")

        # 입력받은 정보를 리스트에 추가
        card = [name, email, phone, affiliation]
        cards.append(card)
        print("\n명함이 저장되었습니다.\n")

    # 2번 선택: 명함 수정
    elif choice == '2' :
        print("\n[ 명함 수정 ]")
        named = input("수정할 명함의 이름을 입력하세요.") # 이름을 입력하세요
        # 해당 이름의 card가 나오게 한다. 매우 어려움 ㅜㅜ
        print("1. 이름 2. 이메일 3. 전화번호 4. 소속(학교/직장)") # 수정 항목을 프린트한다.
        field = input("수정할 항목을 선택해주세요: ") # 다음 내용을 인풋한다. "수정할 항목을 선택해주세요: "
        
        if filed == '1':
            cards[] #"새로운 이름을 입력해주세요: "
        elif field == '2':
            cards[index][1] = input("새로운 이메일을 입력해주세요: ")
        elif field == '3':
            cards[index][2] = input("새로운 전화번호를 입력해주세요: ")
        elif field == '4':
            cards[index][3] = input("새로운 소속(학교/직장)을 입력해주세요: ")
        else:
            print("잘못된 입력입니다.")

        print("\n명함이 수정되었습니다.\n")

    # 3번 선택: 명함 삭제
    elif choice == '3':
         print("\n[ 명함 삭제 ]")




