import string
#intro
print("Welcome to this game of hangman! You get 5 attempts to guess the secret word. You can guess just a letter or the whole word in one go, enjoy!")
# define secret word
secret_word = "hangman"
correct_response=list(secret_word)
def progress(secret_word=secret_word):
    length = len(secret_word)
    answer_progress = []
    for i in range(length):
        answer_progress.append("_")
    print("Here's your progress: " +str(answer_progress))

progress()
#define number of lives
lives =4
# Function to pose the question and get response
def ask_question(lives=lives):
    guess = str(input("What letter do you think is in the word? ")).lower()
    return guess

#Function to call if incorrect answer is given
def lose_a_life(lives=lives):
    lives -=1
    return lives

guess = ask_question()
while lives >0:
#check if letter is in the chosen word
    for letter in guess:
        if letter not in string.ascii_letters:
            print("Thats not a letter! Try again.")
            guess = ask_question()

    if guess in correct_response:
        print(str(guess) +"? " + "Thats in there! Go again!")
        correct_response = [i for i in correct_response if i != guess]
        guess = ask_question()

    elif guess == secret_word:
        lives = 0
        print("Thats right, you guessed the word! Congrats")
        break

    elif len(guess) > 1:
        print("Thats not the full word, you lose a life")
        lives = lose_a_life()
        guess = ask_question()

    else:
        print("Its not in there! You lose a life!")
        print("You have " + str(lives) + " lives left.")
        lives-=1
        guess=ask_question()
        if lives == 0:
            print("Sorry thats all your guesses! The answer was actually " + str(secret_word))

print("Thats it, hope you had fun")