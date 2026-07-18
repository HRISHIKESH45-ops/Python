import os
import random as rn

from playsound import playsound

current_dir = os.path.dirname(os.path.abspath(__file__))
win = os.path.join(current_dir, "win.mp3")
lose = os.path.join(current_dir, "lose.mp3")
tie = os.path.join(current_dir, "tie.mp3")
exit = os.path.join(current_dir, "exit.mp3")

print("WELCOME TO THE ISHOWSPEED ROCK-PAPER-SCISSORS SHOWDOWN!!!")
print("SUUUUUWIIIII! PLAY UNTIL YOU WIN OR RAGE QUIT!\n")

count = 0

while True:
    try:
        user_input = int(input("Enter a choice (1=Rock, 2=Paper, 3=Scissor, 4=Exit): "))
    except ValueError:
        print(
            "ARE YOU SERIOUS RIGHT NEOW BRO?! That's not a number! Enter a valid integer!...\n"
        )
        continue

    if user_input < 1 or user_input > 4:
        print("BRO, CHOOSE BETWEEN 1 AND 4! WHAT ARE YOU DOING?!")
        print("Stop acting like an NPC and enter a valid value! *barks*\n")
        continue
    elif user_input == 4:
        print("No way you are leaving... BYE! *punches camera*")
        try:
            playsound(exit)
        except Exception:
            print("\n[Speed Audio Error]: The sound file is missing, bro!")
        break
    else:
        computer_choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
        cho = rn.choice([1, 2, 3])
        # cho =  rn.randint(1,3)
        count += 1

        if user_input == cho:
            print(f"IShowSpeed chose: {computer_choices[user_input]}")
            print(f"The NPC Computer chose: {computer_choices[cho]}")
            print("A TIE?! ARE YOU SERIOUS RIGHT NEOW BRO?! Try again!\n")
            try:
                playsound(tie)
            except Exception:
                print("\n[Speed Audio Error]: The sound file is missing, bro!")
            continue

        elif (
            (user_input == 1 and cho == 3)
            or (user_input == 2 and cho == 1)
            or (user_input == 3 and cho == 2)
        ):
            print(f"IShowSpeed chose: {computer_choices[user_input]}")
            print(f"The NPC Computer chose: {computer_choices[cho]}\n")
            print(
                f"SEWUUUUUUUIIIIIIII!!! YOU BEAT THE NPC IN {count} ATTEMPTS!!! CRISTIANO RONALDO GOAT!!!"
            )
            try:
                playsound(win)
            except Exception:
                print("\n[Speed Audio Error]: The sound file is missing, bro!")
            break

        else:
            print(f"IShowSpeed chose: {computer_choices[user_input]}")
            print(f"The NPC Computer chose: {computer_choices[cho]}")
            print("WRONG! YOU LOST! *BARKS FURIOUSLY* WUFF WUFF WUFF! Try again!\n")
            try:
                playsound(lose)
            except Exception:
                print("\n[Speed Audio Error]: The sound file is missing, bro!")
