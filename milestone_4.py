import random
my_word_list = ["raspberry","strawberry","blueberry","banana","guava"]


class Hangman:
    def __init__(self, word_list, num_lives=5):
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
            self.num_letters += -1
            print(self.word_guessed)
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:
            guess = (input("Guess a letter\n")).lower()
            if len(guess)!=1 or  not(guess.isalpha()):
                print(f"Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You alread tried the letter {guess}")
            else:
                Hangman.check_guess(self, guess)
                self.list_of_guesses.append(guess)
                break     
                    
    
x=Hangman(my_word_list)
x.ask_for_input()


# s = 'python is fun'
# c = 'n'
# print([pos for pos, char in enumerate(s) if char == c])