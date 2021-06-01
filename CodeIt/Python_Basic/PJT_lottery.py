from random import randint


def generate_numbers(n):
    num = []
    for i in range(n):
        a = randint(1,46)
        if a not in num:
            num.append(a)
        
    return list(num)


def draw_winning_numbers():
    win = []
    while len(win) < 7:
        a = randint(1,45)
        if len(win) < 6:
            if a not in win:
                win.append(a)
        else:
            win = sorted(win)
            if a not in win:
                win.append(a)
    return list(win) 

def count_matching_numbers(list_1, list_2):
    i = 0
    for j in list_1:
        if j in list_2:
            i += 1
    return i
    

def check(numbers, winning_numbers):
    a = count_matching_numbers(numbers,winning_numbers)
    b = count_matching_numbers(numbers,winning_numbers[:5])
    if a > 5 :
        if winning_numbers[-1] not in numbers:
            earn = 1000000000
        else:
            earn = 50000000
    elif b > 4 :
        earn = 1000000
    elif b > 3 :
        earn = 50000
    elif b > 2:
        earn = 5000
    else:
        earn = 0
    return earn

