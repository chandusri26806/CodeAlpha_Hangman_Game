import random
words=["python","computer","program","developer","coding"]
word=random.choice(words)
guessed_letters=[]
wrong_guesses=0
max_wrong_guesses=6
print("WELCOME TO HANGMAN")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")
display_word=["_"]*len(word)
while wrong_guesses<max_wrong_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/",max_wrong_guesses)
    guess=input("Enter a letter: ").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i]==guess:
                display_word[i]=guess
    else:
        wrong_guesses+=1
        print("Wrong guess!")
if "_" not in display_word:
    print("\n Congratulations!")
    print("You guessed the word:",word)
else:
    print("\nGame Over!")
    print("The correct word was:",word)
