

from dataclasses import replace


# num = {
#     'zero':'0',	
#     'one' : '1',
#     'two' : '2',
#     'three' : '3',
#     'four': '4',
#     'five': '5',
#     'six' : '6',
#     'seven':'7',
#     'eight':'8',
#     'nine' : '9',
# }


# s= input()
# s1= s

# for k,v in num.items():
#     if k in s :
#        s1 = s1.replace(k,v)

# print(s1)




def solution(s= input()):
    num = {
        'zero':'0',	
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four': '4',
        'five': '5',
        'six' : '6',
        'seven':'7',
        'eight':'8',
        'nine' : '9',
    }


    s= input()
    s1= s

    for k,v in num.items():
        if k in s :
            s1 = s1.replace(k,v)

    
    return s1



