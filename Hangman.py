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
    return answer_progress

answer_progress  = progress()
# Define number of lives
lives =4
# Function to pose the question and get response
def ask_question(lives=lives):
    guess = str(input("What letter do you think is in the word? ")).lower()
    return guess

# Function to call if incorrect answer is given
def lose_a_life(lives=lives):
    lives -=1
    return lives

guess = ask_question()

# If the user still has a life left, run the sequence
while lives >0:
    count = 0
    # check if letter is in the chosen word
    [print("Thats not a letter! Try again.") for letter in guess if letter not in string.ascii_letters]
    guess = ask_question()

    # create the visual progression towrds the answer
    for i in secret_word:
        if i == guess:
            answer_progress[count] = str(i)
        count+=1

    # If the guess is correct, reduce the list, until its empty and the player wins. Show their progress.
    if guess in correct_response:
        print(str(guess) +"? " + "Thats in there! Go again!")
        correct_response = [i for i in correct_response if i != guess]
        print("Heres your progress: " +str(answer_progress))
        if correct_response == []:
            print("Congratulations, you got there! It was..." + str(secret_word) +"!")
            break
        guess = ask_question()

    # If they guess the word entirely, end the game by setting lives to 0
    elif guess == secret_word:
        lives = 0
        print("Thats right, you guessed the word! Congrats")
        break
    # If user guesses a word, which isnt the correct answer, they lose a life
    elif len(guess) > 1:
        print("Thats not the full word, you lose a life")
        lives = lose_a_life()
        guess = ask_question()

    # User guesses incorrectly, they lose a life. If they run out by this method, end the game
    else:
        print("Its not in there! You lose a life!")
        print("You have " + str(lives) + " lives left.")
        lives-=1
        guess=ask_question()
        if lives == 0:
            print("Sorry thats all your guesses! The answer was actually " + str(secret_word))

print("Thats it, hope you had fun")