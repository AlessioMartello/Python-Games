import string
#intro
print("Welcome to this game of hangman! You get 5 attempts to guess the secret word. You can guess just a letter or the whole word in one go, enjoy!")
# define secret word
secret_word = "hangman"
correct_response=list(secret_word)
#define number of lives
lives =4
# Person enters a letter
def ask_question(lives=lives):
    guess = str(input("What letter do you think is in the word? ")).lower()
    if guess==secret_word:
        lives=0
        print( "Thats right, you guessed the word! Congrats")
        return lives, guess

    elif len(guess) > 1:
        print("Thats not the full word")
        return lives, guess
    else:
        for letter in guess:
            if letter not in string.ascii_letters:
                print("Thats not a letter! Try again.")
                lives, guess = ask_question()
        return lives, guess

lives, guess = ask_question()
while lives >0:
#check if letter is in the chosen word

    if guess in correct_response:
        print(str(guess) +"? " + "Thats in there! Go again!")
        correct_response = [i for i in correct_response if i != guess]
        print(correct_response)
        lives, guess = ask_question()

    else:
        print("Its not there! You lose a life!")
        print("You have " + str(lives) + " lives left.")
        lives-=1
        lives, guess=ask_question()
        if lives == 0:
            print("Sorry thats all your guesses! The answer was actually " + str(secret_word))

print("Thats it, hope you had fun")