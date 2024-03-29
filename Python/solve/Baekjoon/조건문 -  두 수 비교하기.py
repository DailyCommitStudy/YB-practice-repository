# 문제 설명
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하는 문제
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

# 풀이
# 두 수를 비교하는 것은 쉬우나 공백 한 칸으로 구분하여 입력받는 것을 실패하여 검색함.
# split()함수 - 사용 시 공백을 기준으로 두 변수를 나누어 줌.
A, B = input('').split()
A, B = int(A), int(B)
if A > B:
    print('>')
elif A < B :
    print('<')
else :
    print('==')
