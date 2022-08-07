# 문제를 읽고 이해한다

# m행 n열 그리드가 존재
# 그리드에는 박스가 있다
# 0,0 1,0 2,0 3,0 4,0에 0,0 2,0 4,0에 박스가 있다고 치자
# 4,0위로 차례대로 쌓으면 이동한 거리의 수는 몇칸인가!
# box를 담을 리스트, 열에서 박스의 총 이동 횟수

# box = 1
# space = 0
# # 좌표
# y , x = 2, 0
# # 박스 이동
# # 현재 위치는 0 아래위치는 1 저장
# # 다음 위치 탐색
# # 현재 좌표 아래에 박스가 없어야 한다
# while box_lst [y + 1] [x] != box and  y +1 != m::
#     if box_lst [y + 1] [x] != box
#     box_lst[y][x] = space
#     y += 1

# # 조건 2 박스는 바닥을 벗어나면 안된다.
# #       리스트의 범위를 벗어나면 안된다.
# m, n = 5, 4

# # 현박스는 바닥을 벗어나면 안된다
# # 리스트의 범위를 벗어나면 안된다
# if y +1 != m:

박스 = 1
빈공간 = 0
행_개수, 열_개수 = 5,4

박스_리스트 = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]
]
이동거리 = 0
# 이중 반복문
# 열부터 순회
for x in range(열_개수):
# 행순회 단, 아래에서 위로 탐색을 한다.
    # 4 ->
    for y in reversed(range(행_개수)):
        

        # 만약에 현재 탐색하고 있는 좌표에 박스가 있으면
        if 박스_리스트[y][x] == 박스:
            while y+1 != 행_개수 and 박스_리스트[y+1][x] != 박스:
                박스_리스트[y][x] = 빈공간
                박스_리스트[y+1][x] = 박스
                y += 1
                이동거리 +=1
print(이동거리)
            # # 조건 1. 박스 아래에 박스가 없어야한다.
            # if 박스_리스트[y+1][x] != 박스:

            #     # 조건 2. 박스가 바닥을 벗어나면 안된다
            #     # 리스트의 범위를 벗어나면 안된다.
            #     if y+1 != 행_개수:

