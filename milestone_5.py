import random
my_word_list = ["raspberry","strawberry","blueberry","banana","guava"]

class Hangman:
    def __init__(self, word_list, num_lives=5): #Initialises all the attributes
        self.num_lives = num_lives 
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            index=[pos for pos, char in enumerate(self.word) if char == guess]
            for i in index:
                self.word_guessed[i]=guess
            self.num_letters += -1                  #I changed the 'word_guessed' attribute like this because the in-built indexing only
            print(self.word_guessed)                #returns the first instance, rather than every instance.
        else:
            print(f"Sorry, {guess} is not in the word. Try again.\n")
            self.num_lives += -1
            print(f'You have {self.num_lives} lives left')
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = (input("Guess a letter\n")).lower()
            if len(guess)!=1 or  not(guess.isalpha()):
                print(f"Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You alread tried the letter {guess}")
            else:
                Hangman.check_guess(self, guess)
                break     
                    
    
def play_game(word_list):           #I haven't yet added any kind of display. I think I can work out how since that's just a function of num_lives.
    game=Hangman(word_list)         #I would add it but I think my time can be better spent going onto the other projects. I also already have some
    while True:                     #experience with GUIs since I made like a sudoku-solver.
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters >0:
            Hangman.ask_for_input(game)
        elif game.num_lives != 0 and game.num_letters == 0:
            print(f"Congratulations! You won the game")
            break

play_game(my_word_list)



