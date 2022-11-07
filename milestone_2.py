import random
word_list = ["raspberry","strawberry","blueberry","banana","guava"]
word = random.choice(word_list)

guess=input("Enter a single letter")
if len(guess)==1:
    print("good guess")
else:
    print("Oops! That is not a valid input.")