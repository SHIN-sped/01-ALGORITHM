dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
reset = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            reset += dial.index(i)+3
print(reset)







# it takes 2 sec to dial #1
# the dialing time increases by 1 sec by ascending numbers on dial
#   e.g. dial 1 = 2 sec, dial 2 = 3 sec, dial 9 = 10 sec and dial 0 = 11 sec
# Every time when you press number, the dial will be reset and should start from the beginning

