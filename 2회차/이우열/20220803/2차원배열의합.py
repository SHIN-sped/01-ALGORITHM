import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]

sum_ = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_[i][j] = num[i - 1][j - 1] + sum_[i - 1][j] + \
            sum_[i][j - 1] - sum_[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(sum_[x][y] - sum_[x][j - 1] -
          sum_[i - 1][y] + sum_[i - 1][j - 1])


################

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# num = [list(map(int, input().split())) for _ in range(n)]

# k = int(input())
# sum_list = []

# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     sum_num = 0

#     for a in range(i-1, x):
#         for b in range(j-1, y):
#             sum_num += num[a][b]

#     sum_list.append(sum_num)

# for i in range(k):
#     print(sum_list[i])
