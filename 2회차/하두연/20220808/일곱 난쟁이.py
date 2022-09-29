# 백준 2309

# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

height = []
for i in range(9):
    height.append(int(input()))   # 아홉 난쟁이의 키를 리스트로 받는다

for i in height:
    for j in height:
        if sum(height) - i - j == 100 and i != j:       # 아홉 난쟁이의 키 리스트를 전부 더하고 2명의 값을 뺀 값이 100, 9명의 키는 모두 다르기에 i = j
            
            height.remove(i)
            height.remove(j)

height.sort()                                           # 오름차순 정렬

for i in height:
    print(i)

