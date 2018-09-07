import random

class Number:
    def __init__(self):
        self.num = 0
    def generateNum(self):
        self.num = random.randint(1,10)
        return self.num

def main():
    newNum = Number()
    answer = Number.generateNum(newNum)
    guess = int(input('Guess a number from 1 to 10: '))

    while guess != answer:
        if guess > answer:
            print('Too High')
        elif guess < answer:
            print('Too Low')
        guess =int(input('Try Again: '))

    print('Correct!')


main()
