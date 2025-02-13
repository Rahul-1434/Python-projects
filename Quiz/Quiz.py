from database import questions
from database import options

def check(ans,correct_option):
    if ans==correct_option:
        return True
    return False

print("**************************")
print("Welcome to My Quiz Game !!!")
l=['A','B','C','D']
score=0
for i in range(len(questions)):
    print("*******************")
    print(i+1,")",questions[i]["text"])
    for j in range(len(options[i])):
        print("    ",options[i][j])
    ans=input("Enter your Answer(A/B/C/D): ").upper()
    if ans in l:
        x=check(ans,questions[i]["answer"])
        if x:
            score+=1
            print("Correct Answer")
        else:
            print("Incorrect Answer")
            print(f"The correct answer is {questions[i]["answer"]}")
    else:
        print("Invalid Option!")
    print(f"your current score is {score}/{i+1}")
print()
print("*****************************************************")
print(f"Your have given {score} correct answer")
print(f"Your score is {(score/len(questions))*100}%")
