# https://www.acmicpc.net/problem/2577

# 세 개의 자연수 A, B, C가 주어질 때
# A * B * C 를 계산한 결과에 0부터 9까지 각각 숫자가 몇 번씩 쓰였는지 구하는 프로그램
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력
# 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가
# 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력

import sys

sys.stdin = open("0_숫자의개수.txt")

# 예를 들어 A = 150, B = 266, C = 427 이라면
# A × B × C = 150 × 266 × 427 = 17037300 이 되고
# 계산한 결과 17037300 에는 
# 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다

A = int(input())
B = int(input())
C = int(input())

# A, B, C를 곱한 값을 문자열로 변환 후 list 묶음
Multiplication = list(str(A * B * C))

# for문을 이용해 i = 0 ~ 9까지
# 문자열만 사용 가능한 함수인 count를 사용
# i를 문자열로 바꾼 뒤 Multiplication 리스트 안에
# 그 수가 있는지 확인하고 그 수만큼 print
for i in range(10):
    print(Multiplication.count(str(i)))


# 정수(int)끼리 곱한 값을 문자열로 바꾼 뒤
# list 함수를 이용해서 리스트화하고
# count 함수를 사용하기 위해
# 정수가 아닌 문자열로 바꾼 뒤 출력해야 함