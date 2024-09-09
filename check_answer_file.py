def check_answer(answer, guess):
    if answer == guess:
        print("Answer is CORRECT !")
        return 1
    else:
        print("Answer is WRONG !")
        return 0