# 박스 🚨
# 문제 : 모든 박스가 이동한 거리 구하기

N = int(input())
answer = []
for _ in range(N):
    ls = list(map(int, input().split()))
    metrix = [list(map(int, input().split())) for _ in range(ls[0])]
    array = [0] * ls[1]
    cnt = 0
    for i in metrix:
        temp = 0
        for k in i:
            if(k == 1):
                array[temp] += 1
            else:
                cnt += array[temp]
            temp += 1
    answer.append(cnt)
for i in answer:
    print(i)
