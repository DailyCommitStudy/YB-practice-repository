# 문제 설명
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

def solution(number, n, m):
    answer = 0
    if number % n == 0:
        if number % m == 0:
            answer = 1
        else :
            answer = 0
    else :
        answer = 0
    return answer

# if문에 and를 써서 더 간단하게 할 수 있음
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    return 0