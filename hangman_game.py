import random

with open('word_list.txt') as f:    my_word_list = [ line.strip() for line in f ]


class Hangman:

    def __init__(self, word_list, num_lives=7): #Initialises all the attributes
        
        self.num_lives = num_lives 
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


    def check_letter(self, guess):
    
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            index=[pos for pos, char in enumerate(self.word) if char == guess]

            for i in index:
                self.word_guessed[i]=guess
            self.num_letters -= 1                  
            print(self.word_guessed)

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.\n')
            print(self.word_guessed)
        self.list_of_guesses.append(guess)

    def check_word(self, guess):

        if guess == self.word:
            print("Correct word!")
            self.num_letters = 0
        else:
            print("That word is not the word!")
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.\n')
            print(self.word_guessed)
        self.list_of_guesses.append(guess)


    def ask_for_input(self):

        while True:
            guess = (input("Guess a letter\n")).lower()

            if  not(guess.isalpha()):
                print(f"Invalid letter or word. Please, enter a single alphabetical character or a word.")

            elif guess in self.list_of_guesses:
                print(f"You alread tried the letter {guess}")
                
            elif len(guess) == 1:
                Hangman.check_letter(self, guess)
                break     
            else:
                Hangman.check_word(self,guess)
                break
    
def play_game(word_list):           

    game = Hangman(word_list)         
    print(game.word_guessed)
    print(f"You have {game.num_lives} lives.")
    while True:                     

        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was '{game.word}'")
            break

        elif game.num_letters >0:
            Hangman.ask_for_input(game)

        elif game.num_lives != 0 and game.num_letters == 0:
            print(f"Congratulations! You won the game. The word was {game.word}.")
            break



play_game(my_word_list)



