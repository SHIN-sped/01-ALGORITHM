#-*- coding: utf-8 -*-
# 일 년 동안 세계일주를 하던 영식이는 여행을 하다 너무 피곤해서 근처에 있는 코레스코 콘도에서 하룻밤 잠을 자기로 하고 방을 잡았다.

# 코레스코 콘도에 있는 방은 NxN의 정사각형모양으로 생겼다. 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다. 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다. 영식이가 누울 수 있는 자리에는 조건이 있다. 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다. 가로로 누울 수도 있고 세로로 누울 수도 있다. 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다. (중간에 어정쩡하게 눕는 경우가 없다.)



# 만약 방의 구조가 위의 그림처럼 생겼다면, 가로로 누울 수 있는 자리는 5개이고, 세로로 누울 수 있는 자리는 4개 이다. 방의 크기 N과 방의 구조가 주어졌을 때, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.



# n=int(input())

# matrix =[list(input()) for __ in range(n)]


# w_cnt=0
# l_cnt=0
# for wlist in matrix:
#     wjo = ''.join(wlist)
#     w_cnt+= wjo.count('..X')
#     w_cnt+= wjo.count('X..')
#     w_cnt-= wjo.count('X..X')
#     if 'X' not in wjo and '..' in wjo:
#         w_cnt+=1

# for y in range(n):
#     llist= []
#     for x in range(n):
#         llist.append(matrix[x][y])
#     ljo=''.join(llist)
#     l_cnt+= ljo.count('..X')
#     l_cnt+= ljo.count('X..')
#     l_cnt-= ljo.count('X..X')
#     if 'X' not in ljo and '..' in ljo:
#         l_cnt+=1

 
# print(f'{w_cnt} {l_cnt}')
                                    # if matrix[x][y] =='X':
                                    #     ljo=''.join(llist)
                                    #     if '..' in ljo:




    # for w in lists:
    #     # jow= 
    #     # if '.' in w :
    #     #     w_cnt+= 1\


n=int(input())

w_cnt=0
l_cnt=0
matrix =[list(input()) for __ in range(n)]

for i in matrix:
    jum1= 0
    for j in i:
        if j== '.': 
            jum1+=1
        elif j == 'X':
            if jum1>= 2:
                w_cnt+=1
                jum1=0
            else:
                jum1=0
    if jum1>= 2 :
        w_cnt+=1


for x in range(n):
    jum2=0
    for y in range(n):
        if matrix[y][x] == '.':
            jum2+=1
        elif matrix[y][x] == 'X':
            if jum2>= 2:
                l_cnt+=1
                jum2=0
            else:
                jum2=0
    if jum2>= 2 :
        l_cnt+=1
print(w_cnt,l_cnt)