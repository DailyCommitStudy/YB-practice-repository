# 문제 설명
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

# 변수 설정
a = [int(input()) for _ in range(10)]
rest = []

# 1. a의 각 요소에 대해 % 연산을 진행
# 2. 해당 값을 리스트에 집어넣음
# 3. 중복을 없앤 후 len()

# 1. a의 각 요소에 대해 % 연산을 진행
for i in range(10) :
    # rest = [] - 요렇게 하면 반복문 돌 때마다 초기화된다고 몇 번 실수해놓고 또 실수할 뻔한 YB(..)
    # 2. 해당 값을 리스트에 집어넣음
    rest += [a[i] % 42]
# 3. 중복을 없앤 후 len()
'''
리스트 중복 없애는 법(구글링)
1. set 사용
새로운 리스트 = list(set(기존 리스트))
* 사용 시 순서가 재정렬됨. 순서를 유지하고 싶을 경우엔 2번 사용
2. for문과 append 사용
새로운 리스트 = []
for element in 기존 리스트 :
    if element not in 새로운 리스트 : (오 과제 안 낸 사람 문제 코드와 비슷함)
        새로운 리스트.append(element)
* 인덱스 순서대로 반복문을 돌기 때문에 순서를 유지하면서 중복을 제거함.
'''
rest_not_dup = list(set(rest))
print(len(rest_not_dup))