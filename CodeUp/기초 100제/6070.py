# [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
m = int(input())

if m // 3 == 1:
    print("spring")
elif m // 3 == 2:
    print("summer")
elif m // 3 == 3:
    print("fall")
else:
    print("winter")