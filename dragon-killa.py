import random
import csv

def question_generator():
    num_1 = random.randint(1,12)
    num_2 = random.randint(1,10)
    num_3 = random.randint(1,20)
    num_4 = random.randint(1,20)
    print("What is",num_1,"x",num_2,"+",num_3,"-",num_4,"?")
    print("")
    num_array = [num_1,num_2,num_3,num_4]
    return num_array

def check(num_1,num_2,num_3,num_4):
    ans_user = int(input("Enter here: "))
    ans_comp = num_1 * num_2 + num_3 - num_4
    if ans_user == ans_comp:
        status = "Correct"
    else:
        status = "Wrong"
    return status

def q_math():
    num_1_h = random.randint(1,60)
    num_2_h = random.randint(1,10)
    num_3_h = random.randint(1,60)
    num_4_h = random.randint(1,60)
    num_5_h = random.randint(1,60)
    print("What is",num_1_h,"x",num_2_h,"+",num_3_h,"-",num_4_h,"+",num_5_h,"?")
    print("")
    num_array_h = [num_1_h,num_2_h,num_3_h,num_4_h,num_5_h]
    return num_array_h

def check_h(num_1_h,num_2_h,num_3_h,num_4_h,num_5_h):
    ans_user_h = int(input("Enter here: "))
    ans_comp_h = num_1_h * num_2_h + num_3_h - num_4_h + num_5_h
    if ans_user_h == ans_comp_h:
        status_h = "Correct"
    else:
        status_h = "Wrong"
    return status_h

def q_vocab():
    file = open("vocab.csv","r")
    reader = csv.reader(file)
    rows = list(reader)
    row_csv = random.randint(0,14)
    print("What is the meaning of", rows[row_csv][0], "?")
    print("")
    print("[a] ", rows[row_csv][1])
    print("")
    print("[b] ", rows[row_csv][2])
    print("")
    print("[c] ", rows[row_csv][3])
    print("")
    print("[d] ", rows[row_csv][4])
    return row_csv

def check_v(row_csv):
    file = open("vocab.csv","r")
    reader = csv.reader(file)
    rows = list(reader)
    print("")
    vocab_user = input("Enter the letter here: ")
    vocab_comp = rows[row_csv][5]
    if vocab_user == vocab_comp:
        status_v = "Correct"
    else:
        status_v = "Wrong"
    return status_v

def battle(weapon):
    questions_wrong = 0
    questions_total = 0
    print("--------------------------------------------------")
    if weapon == "Butterknife":
        while questions_wrong < 3 and questions_total < 8:
            print("--------------------------------------------------")
            print("Question",questions_total + 1)
            questions_total = questions_total + 1
            choose_questions = random.randint(0,1)
            if choose_questions == 0:
                print("")
                print("The game has chosen a math question for you! Now, answer the question to have a chance of hitting the dragon: ")
                num_array_h = q_math()
                status_h = check_h(num_array_h[0],num_array_h[1],num_array_h[2],num_array_h[3],num_array_h[4])
                print("")
                if status_h == "Correct":
                    print("Whoosh! You hit one of the dragon's body parts. Don't get too many questions wrong!")
                    print("")
                else:
                    questions_wrong = questions_wrong + 1
                    print("Oh no! You missed hitting the dragon. It blew a fire breath and it damaged you. You have answered",questions_wrong,"questions wrongly, try not to hit 3!")
                    print("")
                if questions_total == 8:
                    print("After receiving so much damage, the dragon falls to the ground, dead. You successfully killed the dragon, victory is yours! The end!")
            else:
                print("--------------------------------------------------")
                print("The game has chosen a vocabulary question for you! Now, answer the question to have a chance of hitting the dragon: ")
                row_csv = q_vocab()
                status_v = check_v(row_csv)
                print("")
                if status_v == "Correct":
                    print("Whoosh! You hit one of the dragon's body parts. Don't get too many questions wrong!")
                    print("")
                else:
                    questions_wrong = questions_wrong + 1
                    print("Oh no! You missed hitting the dragon. It blew a fire breath and it damaged you. You have answered",questions_wrong,"questions wrongly, try not to hit 3!")
                    print("")
                if questions_total == 8:
                    print("After receiving so much damage, the dragon falls to the ground, dead. You successfully killed the dragon, victory is yours! The end!")
        if questions_wrong == 3:
            print("--------------------------------------------------")
            print("You fall down to the ground due to getting 3 questions wrong. The dragon finishes you off with a sharp nab of its legs. You failed to defeat the dragon. The end! You can always try another time.")
    else:
        while questions_wrong < 3 and questions_total < 6:
            print("--------------------------------------------------")
            print("Question",questions_total + 1)
            questions_total = questions_total + 1
            choose_questions = random.randint(0,1)
            if choose_questions == 0:
                print("")
                print("The game has chosen a math question for you! Now, answer the question to have a chance of hitting the dragon: ")
                num_array_h = q_math()
                status_h = check_h(num_array_h[0],num_array_h[1],num_array_h[2],num_array_h[3],num_array_h[4])
                print("")
                if status_h == "Correct":
                    print("Whoosh! You hit one of the dragon's body parts. Don't get too many questions wrong!")
                    print("")
                else:
                    questions_wrong = questions_wrong + 1
                    print("Oh no! You missed hitting the dragon. It blew a fire breath and it damaged you. You have answered",questions_wrong,"questions wrongly, try not to hit 3!")
                    print("")
                if questions_total == 6:
                    print("After receiving so much damage, the dragon falls to the ground, dead. You successfully killed the dragon, victory is yours! The end!")
            else:
                print("--------------------------------------------------")
                print("The game has chosen a vocabulary question for you! Now, answer the question to have a chance of hitting the dragon: ")
                row_csv = q_vocab()
                status_v = check_v(row_csv)
                print("")
                if status_v == "Correct":
                    print("Whoosh! You hit one of the dragon's body parts. Don't get too many questions wrong!")
                    print("")
                else:
                    questions_wrong = questions_wrong + 1
                    print("Oh no! You missed hitting the dragon. It blew a fire breath and it damaged you. You have answered",questions_wrong,"questions wrongly, try not to hit 3!")
                    print("")
                if questions_total == 6:
                    print("After receiving so much damage, the dragon falls to the ground, dead. You successfully killed the dragon, victory is yours! The end!")
        if questions_wrong == 3:
            print("--------------------------------------------------")
            print("You fall down to the ground due to getting 3 questions wrong. The dragon finishes you off with a sharp nab of its legs. You failed to defeat the dragon. The end! You can always try another time.")

print("Welcome to Dragon Killer! Your mission is to kill the dragon of evil and save your city while learning math and english. Isn't that fun? (It's not) Do you accept the challenge? Enter 'yes' or 'no'.")
print("--------------------------------------------------")

choice_user = input("Enter here: ")

if choice_user == "yes":
    print("")
    print("Great! Let's begin.")
    print("--------------------------------------------------")
    print("You arrive at the Dragon's Lair. But before you go in, you'll need to get some weapons! Head to the arsenal store nearby.")
    print("")
    print("You reach the arsenal. But before you reach out to touch the weapons, a board appears infront of you and displays a math question. You'll need to solve it to get better weapons! Answer the question:")
    print("")

    num_array = question_generator()
    status = check(num_array[0],num_array[1],num_array[2],num_array[3])
    if status == "Correct":
        print("--------------------------------------------------")
        print("Good job on answering correctly! You get a sword as your reward. Go back to the Dragon's Lair.")
        weapon = "Sword"
    else:
        print("--------------------------------------------------")
        print("Oops! Looks like you answered wrongly. You get a butterknife as your reward. Go back to the Dragon's Lair.")
        print("")
        weapon = "Butterknife"
    print("You arrive back at the lair entrance. Once you peek in, you realize there are a lot of traps!  But you go in anyway.")
    print("")
    print("To get through the first trap with walls shooting out flaming fire arrows, you'll need to solve a math question. Answer the question:")
    print("")

    num_array = question_generator()
    status = check(num_array[0],num_array[1],num_array[2],num_array[3])
    if status == "Correct":
        print("--------------------------------------------------")
        print("Wow! You made it through the first trap, nice job! But there's still two more traps, will you make it past them?")
        print("")
        print("The next trap is a laser room. If you touch them, you will die and fail your mission. Like always, you have to solve a math question to get past! Answer the question:")
        print("")

        num_array = question_generator()
        status = check(num_array[0],num_array[1],num_array[2],num_array[3])
        if status == "Correct":
            print("--------------------------------------------------")
            print("Good job on getting past the second trap! Moving on to the third and final one!")
            print("")
            print("Last but not least is the final trap! This room is filled with poisonous gas that can kill you in seconds. Fast, answer the question:")
            print("")

            num_array = question_generator()
            status = check(num_array[0],num_array[1],num_array[2],num_array[3])
            if status == "Correct":
                print("--------------------------------------------------")
                print("Yay, you made it past the traps successfully! Now it's time for the hard part: defeating the dragon.")
                print("")
                print("You go in the battleground where the dragon is. As you see the dead bodies of other people who tried to kill the dragon, you sweat and shiver. The dragon greets you with a blow of its fire breath.")
                print("")
                print("To defeat the dragon, you'll need to solve a few math and vocabulary questions. Depending on your weapon you got from the start, you will have a certain amount of questions you will need to answer. If you answer 3 questions wrongly, you will fail to defeat the dragon and die. Will you successfully kill the dragon?")
                print("")
                print("It's now or never. Your time begins now!")
                battle(weapon)
            else:
                print("--------------------------------------------------")
                print("You didn't answer the question correctly, and you die of inhaling too much poisonous gas. The end! You can always try another time.")
        else:
            print("--------------------------------------------------")
            print("While you think that you're going to make it past, you lose your balance and die from touching the lasers. The end! You can always try another time.")
    else:
        print("--------------------------------------------------")
        print("Unfortunately, you get shot by one of the flaming arrows and get burned to death. The end! You can always try another time.")
else:
    print("How could you? This is a one in a lifetime oppurtunity. You big coward.")
