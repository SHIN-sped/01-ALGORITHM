N = int(input())
# 1 <= N <= 100 별 갯수
# 첫째줄부터 N번째 줄까지 차례대로 별
for i in range(1, N+1): # 1부터 N 까지 
    print(f'{"*"*i:>{N}}') # 별을 i개만큼 출력 하는데 오른쪽정렬
    print('{:>{n}}'.format('*'*i,n=N))