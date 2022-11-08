import random
my_word_list = ["raspberry","strawberry","blueberry","banana","guava"]


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives 
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        