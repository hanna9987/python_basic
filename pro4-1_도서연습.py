import sys

library = {'안녕': ['호호', '기술'], '잘가': ['헤헤', '예술']}

menu = '''\n─────────────────────────
📌 도서관 사용 메뉴 선택    
─────────────────────────
1. 도서 추가 
2. 도서 찾기 
3. 도서 삭제 
4. 도서 수정 
5. 도서 대출 
6. 도서 반납 
7. 도서 목록 보기 (전체목록보기>대출가능한 목록보기)
8. 도서관 이용 종료 
─────────────────────────'''

while True:
    print(menu)
    choice = input("\n이용하실 메뉴를 선택해주세요 >>> ")
    
    if choice == '1': 
        print('\n[✅ 도서 추가]')
        while True:
            title = input('책제목: ')
            if title == '':
                print('⏪ 도서를 추가하지 않고 메뉴로 돌아갑니다.')
                break
            if title in library:
                print('💡 이미 존재하는 도서입니다.')
                print('  추가를 원하지 않으시면 "Enter"를 입력하세요.')
                continue
            else :
                break

        if title != '': #if title: 제목이 비어있지 않다면
            author = input('저자: ')
            while True:
                category = input('분류(인문/과학/예술/기술): ')
                categories = ['인문','과학','예술','기술']
                if category in categories:
                    break
                print('❌ 올바른 분류명을 입력하세요.\n') # if 만족하지 못하면 자동으로 출력

            library[title] = [author, category]
            print(f'\n✅ [{title}] 도서가 추가되었습니다.')
            print(library)


    elif choice == '2':
        print('\n[🔍 도서 찾기]')

    elif choice == '3':
        print('\n[🗑️ 도서 삭제]')
        while True:
            title = input('삭제할 도서명을 입력하세요. \n👉 ').strip()
            if title in library:
                while True:
                    confirm = input('⚠️ 위 도서를 정말로 삭제 하시겠습니까? Y / N : ').strip().upper()
                    if confirm == 'Y':
                        print(f'🗑️  [{title}] 도서가 삭제되었습니다.')
                        del library[title]
                        break
                    elif confirm == 'N':
                        print("⏪ 삭제를 취소했습니다.")
                        break
                    else:
                        print('❌ 올바른 입력이 아닙니다. 다시 입력하세요.')
                        continue
                break
            else :
                print('❌ 올바른 도서명을 입력하세요.\n')

    elif choice == '4':
        print('\n[🔄 도서 수정]')
        title = input('수정할 도서명을 입력하세요. \n👉 ').strip()

                

    elif choice == '5':
        print('\n[📖 도서 대출]')

    elif choice == '6':
        print('\n[📤 도서 반납]')

    elif choice == '7':
        print('\n[📚 도서 목록 보기]')
        if library:
            for k, v in library.items():
                print(f'🔹 제목: {k} │ 저자: {v[0]} │ 분류: {v[1]}')

    elif choice == '8':
        print('\n[도서관 이용을 종료합니다 🔚]')
        sys.exit()

    else:
        print('💡 메뉴선택을 잘못하셨습니다.')

