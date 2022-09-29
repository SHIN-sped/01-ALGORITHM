n, m = 8, 8

# chess = [list(input()) for _ in range(n)]
chess =[
    ['.', 'F', '.', 'F', '.', '.', '.', 'F'], 
    ['F', '.', '.', '.', 'F', '.', 'F', '.'], 
    ['.', '.', '.', 'F', '.', 'F', '.', 'F'], 
    ['F', '.', 'F', '.', '.', '.', 'F', '.'], 
    ['.', 'F', '.', '.', '.', 'F', '.', '.'], 
    ['F', '.', '.', '.', 'F', '.', 'F', '.'], 
    ['.', 'F', '.', 'F', '.', 'F', '.', 'F'], 
    ['.', '.', 'F', 'F', '.', '.', 'F', '.']
    ]

#하얀판 (0,0) (0,2) (0,4) (0,6) (1,1) (1, 3) ... 행렬의 인덱스 더해서 짝수면 흰칸
#인덱스의 합이 짝수인 칸에 말이 있는지 없는지 확인해서 카운트하기

cnt = 0

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0 or (i + j) == 0:
            if chess[i][j] == 'F':
                cnt += 1
print(cnt)