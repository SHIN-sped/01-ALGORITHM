# https://www.acmicpc.net/problem/10995
a, b = input().split()
if int(a) > int(b):
    print('>')
elif int(a) < int(b):
    print('<')
else:
    print('==')