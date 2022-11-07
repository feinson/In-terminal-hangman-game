import random
word_list = ["raspberry","strawberry","blueberry","banana","guava"]
word = random.choice(word_list)

while True:
    guess = (input("Guess a letter\n")).lower()
    if len(guess)==1 and guess.isalpha():
        break
    else:
        "Invalid letter. Please, enter a single alphabetical character."

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")