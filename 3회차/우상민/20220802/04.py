# 백준 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.



li = []
for i in range(int(input())):
    li.append(int(input()))
li.sort()
print(*li, sep='\n')