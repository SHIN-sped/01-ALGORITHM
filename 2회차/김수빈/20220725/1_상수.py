# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = map(int, input().split())

A_reverse = str(A)[::-1]
B_reverse = str(B)[::-1]

if int(A_reverse) > int(B_reverse):
    print(A_reverse)
else:
    print(B_reverse)