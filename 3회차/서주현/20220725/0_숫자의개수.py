# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

for i in range(10) :            ## 출력이 0~9까지 순서대로라서 range를 먼저 썼다.
    cnt = 0
    for j in str(a*b*c) :       ## 스트링으로 비교한다. 
        if str(i) == j :
            cnt += 1
    print(cnt)