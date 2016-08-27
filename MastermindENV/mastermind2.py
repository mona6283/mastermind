import random
import string

class Mastermind:
    def __init__(self, guess='', color=['W', 'P', 'R', 'Y', 'G', 'B'], tries=3,places=4,answer=''):
        self.color =color
        self.tries=tries
        self.places = places
        self.guess = guess
        self.answer=list(answer)

    def secret_choice(self,color):  # computer randomly picks four-color
        selection=''.join(random.sample(color,4))
        self.answer=selection

    def get_guess(self):  # player guesses the colors
        guess = input('Your Guess: ')
        u=guess.upper()
        self.guess=list(u)


    def evaluate(self):# comparison between player's input and secret choice
        blackPeg = 0
        whitePeg = 0


        for i in range (self.places):
            if self.guess[i]==self.answer[i]:
                blackPeg += 1
        print('Black Peg: ',('*'*blackPeg))

        for j in range (self.places):
            if self.guess[j] in self.answer and self.guess[j] != self.answer[j]:
                whitePeg += 1
        print('White Peg: ',('*'*whitePeg))
        print()

    def len_check(self):
        if len(self.guess) != self.places:
            print('+++please choose 4 colors,try again!+++')
            print()
            guess = input('Your Guess: ')
            u = guess.upper()
            self.guess = list(u)

    def repeat_check(self):

        if self.guess[0] == self.guess[1] or self.guess[0] == self.guess[2] or \
                        self.guess[0] == self.guess[3] or self.guess[1] == self.guess[2] or \
                        self.guess[1] == self.guess[3] or self.guess[2] == self.guess[3]:
            print('+++No repeat color, try again!+++')
            print()
            guess = input('Your Guess: ')
            u = guess.upper()
            self.guess = list(u)


    def win_game(self,tries):
        if self.guess == self.answer:
            print('***Congratulation! You completed the game!***')
        if self.guess !=self.answer and tries>3:
            print('+++Sorry! you failed the game!+++')
            print('The correct answer is: ',str(self.answer))

def main():
    tries = 0
    print()
    print('***New game started***')
    print()
    game= Mastermind()
    color = ['W', 'P', 'R', 'Y', 'G', 'B']
    game.secret_choice(color)
    print('<<choose 4 colors among ( White ,Blue ,Red ,Yellow, Green, Purple )>>: ')
    print('<<Enter W as White, B as Blue, R as Red, Y as Yellow and P as Purple>>')
    print()
    game.get_guess()
    while tries < 4:
        game.len_check()
        game.repeat_check()


        for guessed_color in game.guess:
            if guessed_color not in game.color:
                print( '+++your guess must be among these colors ( White ,Blue ,Red ,Yellow,Green,Purple ), try again!+++')
                print()
                tries += 1
                game.get_guess()


        game.evaluate()
        tries += 1
        game.get_guess()
        game.win_game(tries)

main()









