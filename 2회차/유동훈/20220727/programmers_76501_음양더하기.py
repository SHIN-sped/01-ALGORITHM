# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 음양더하기

# 풀이
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        elif signs[i] == False:
            answer -= absolutes[i]
    return answer