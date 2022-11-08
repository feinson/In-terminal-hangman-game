import random
my_word_list = ["raspberry","strawberry","blueberry","banana","guava"]


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives 
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)

        char_list = []
        char_list[:0] = self.word
        char_set = set(char_list)
        self.num_letters=len(char_set)


        self.word_list = word_list
        self.list_of_guesses = []


x=Hangman(my_word_list)