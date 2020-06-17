import string
#intro
print("Welcome to this game of hangman! You get 5 attempts to guess the secret word. You can guess just a letter or the whole word in one go, enjoy!")
# define secret word
secret_word = "hangman"
#define number of lives
lives =4
# Person enters a letter
def ask_question():
    guess = str(input("What letter do you think is in the word? ")).lower()
    for letter in guess:
        if guess not in string.ascii_letters:
            print("thats not a letter! Try again.")
            ask_question()
    return guess

guess = ask_question()

while lives >0:
#check if letter is in the chosen word
    if guess in secret_word:
        print("Thats in there! Go again!")
        guess=ask_question()
            #do something
    else:
        print("Its not there! You lose a life!")
        lives-=1
        guess=ask_question()
        if lives == 0:
            print("Sorry thats all your guesses! The answer was actaully " + str(secret_word))


