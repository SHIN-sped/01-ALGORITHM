count = 0
N = int(input())
i = 1

while True:
    if '666' in str(i):
        count += 1
    
    if count == N:
        print(i)
        break
    
    i+=1