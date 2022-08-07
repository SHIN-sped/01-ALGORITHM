# 백준 5622
# 다이얼 전화기로 전화를 걸고 싶은 번호가 있다면
# 숫자를 하나 누른 다음 금속 핀이 있는 곳까지 시계방향으로 돌려야 함
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고
# 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 함

# 1을 걸려면 총 2초가 필요하다.
# 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다

# 전화 번호를 각 숫자에 해당하는 문자로 외워
# 어떤 단어를 걸 때 각 알파벳에 해당하는 숫자를 걸면 된다
# 예 : UNUCIC는 868242

# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력

import sys
sys.stdin = open('다이얼.txt')

alphabetList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0

for unit in alphabetList:
    #* alphabetList에서 각 요소를 꺼내 한 글자씩 분리
    for i in unit:
        #* 입력 받은 문자를 하나씩 분리
        for x in word:
            #* 두 알파벳이 같으면
            if i == x:
                #* time = time + index + 3
                #* 시간은 맨 위 for문에서 알파벳 리스트의 요소인 nuit 변수의 위치를 찾아서 더함
                #* 위치는 index 함수를 사용
                #* 마지막에 3을 더하는 이유는 다이얼을 돌릴 때
                #* 1을 누르는데 2초가 걸리고 이후에는 1초씩 증가하기 때문
                #* index는 0부터 시작하므로 첫 번째 인덱스는 +3을 하면 정확한 시간을 반환할 수 있음
                time += alphabetList.index(unit) + 3
print(time)
