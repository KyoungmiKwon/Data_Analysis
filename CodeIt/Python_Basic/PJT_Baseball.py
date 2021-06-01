from random import randint

def generate_numbers():

    numbers = []
    while len(numbers) < 3:
        a = randint(0,9)
        if a not in numbers:
            numbers.append(a)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")       
    return numbers  


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 코드를 작성하세요.
    i = 1
    while len(new_guess) < 3:
        
        guess = int(input(f'{i}번째 숫자를 입력하세요.'))

        if guess not in range(1,10):
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요')
        elif guess in new_guess:
            print('중복되는 숫자입니다. 다시 입력하세요.')
        else:
            new_guess.append(guess)
            i += 1
    return new_guess
    

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1
         
    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

print(ANSWER)

# 코드를 작성하세요.
while True:
    GUESS = take_guess()
    s, b = get_score(GUESS, ANSWER)

    print(f'{s}S {b}B \n')
    tries += 1

    if s == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
