# ------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses, guesses)
# ------------------------
def check_answer(answer,guess):

    if answer ==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    

    
# ------------------------
def display_score(correct_guesses, guesses):
    print("----------------------")
    print("RESULTS")
    print("------------------------")

    print("Answers:", end="")
    for i in questions:
        print(questions.get(i),end="")
    print()

    print("Guesses:",end="")
    for i in guesses:
        print(i,end="")
    print()
       
    score =int((correct_guesses/len(questions))*100)
    print("Your score is:"+str(score)+"%")


# --------------------------
def play_again():

    response = input("do you want to play again?:(yes or no): ")
    response=response.upper()

    if response =="YES":
        return True
    else:
        return False
#--------------------------------


questions ={
 "who created python?: ": "A",
 "what year was python created?: ": "B",
 "python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}




options = [["A. Guido van rossum","B.Elon Musk","C.Bill Gates","D.Mark Zuckerburg"],
          ["A.1989","B. 1991","C. 2000","D. 2016"],
          ["A. LOnely Island","B. smosh","c.MOnty python ","D . SNL"],
          ["A. True","B. Fasle","c.sometimes","D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
