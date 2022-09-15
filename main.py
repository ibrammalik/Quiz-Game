print("\nWelcome To My Quiz Game")

score = 0
lives = 3
questions_answer = ["CPU,central processing unit", "RAM,random access memory",
                    "HDD,hard disk drives", "SSD,solid state drives", "CD-ROM,compact disc read only memory"]


def askReady():
    is_ready = input("\nAre You Ready (y/n)? ").lower()
    if (is_ready == "n"):
        quit()


def rules():
    print("\nYou have 3 lives, if you wrong 3 times Game Over")
    print("answer cannot miss spelled, but it can accept either lowercase or uppercase")


def askQuestions(item):
    item_question = item.split(",")[0]
    correct_answer = item.split(",")[1]
    question = "\nWhat is {} stand for ? ".format(item_question)
    user_answer = input(question).lower()
    if (user_answer == correct_answer):
        print("\n==================== CORRECT ====================")
        global score
        score += 1
    else:
        global lives
        lives -= 1
        if (lives == 0):
            print("GAME OVER")
            quit()
        else:
            print("\n================== WRONG!! ==================")
            livesLeft = "\nyou have {} lives left"
            print(livesLeft.format(lives))


rules()
askReady()
for item in questions_answer:
    askQuestions(item)


print("your score ", score/len(questions_answer)*100, "%")
