import sys
sys.stdin = open("5_숫자문자열과영단어.txt")

s = input()

def solution(s):
    
    numbers = {"zero":"0","one":"1","two":"2","three":"3","four":"4",
    "five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    
    answer = s
    
    for key, value in numbers.items():
#         replace() argument 2 must be str, not int
        answer = answer.replace(key, value)
    return int(answer)

print(solution(s))