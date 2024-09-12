from data import questions
import time

def display_score(correct, guesses):
    print("RESULTS")
    time.sleep(1)
    print("----------------------------------------------------------------------------------------------")
    time.sleep(1)
    print("----------------------------------------------------------------------------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()        
    
    score = int((correct/20) * 100)
    finished_time = time.time()
    print("You have scored " + str(score) + "%")