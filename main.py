from data import questions, choices
from check_answer_file import check_answer
from display_score_file import display_score
from play_again_file import play_again
from time_counter import counter
import time



print("Welcome to Chemistry Quiz !!!")
time.sleep(1)
print("There are 20 multiple choice questions in total")
time.sleep(1)
print("After each question and answer is displayed please enter your choice, either 'A', 'B', 'C' or 'D' ")
time.sleep(1)
start_time = time.ctime(time.time())
print("The current time of starting is now " + start_time)
time.sleep(1)
print("Timer starts now, You may now begin !")
time.sleep(1)

def new_game():

    user_guesses = []
    correct_guesses = 0
    question_num = 1

    for x in questions:
        print("----------------------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("----------------------------------------------------------------------------------------------")
        time.sleep(0.5)
        print(str(question_num) + ". " + x)
        for y in choices[question_num - 1]:
            print(y)
        question_num += 1
        user_guess = input("Enter your choice: ").upper()
        user_guesses.append(user_guess)

        correct_guesses += check_answer(questions.get(x), user_guess)

    display_score(correct_guesses, user_guesses)
  

new_game()
while play_again():
    new_game()



    time.time() #current time since epoch