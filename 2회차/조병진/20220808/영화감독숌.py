# 영화감독 숌 🐳
# 문제 : '666'이 들어간 N번째 영화 제목 구하기

N = int(input())

title = 666
cnt = 0
while True:
    if '666' in str(title):  # title에서 666이 나오면 카운트 1씩 증가
        cnt += 1

    if cnt == N:  # 입력값과 같으면 출력하고 멈춤
        print(title)
        break

    title += 1  # 1씩 증가하면서 완전 탐색
