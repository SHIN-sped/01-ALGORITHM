# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

a = int(input())
m = []
while len(m) < a:
    m.append(list(input().strip()))
cnt = 0
score = 0
scores = []
for ii in range(len(m)):
    for i in m[ii]:
        if i == 'O':
            score += (1+cnt)
            cnt += 1
        else:
            cnt = 0
    scores.append(score)
    score = 0
    cnt = 0
for i in range(a):
    print(scores[i])