# game "kaun banega crore pati"
yes = input("DO you want to play Kaun Banega Crore Pati? :")
if yes.lower() == "yes" or yes.lower == "y":
    print("Welcome to Kaun Banega Crore Pati")
    first = input("Which of the following is considered the father of computer science? \n A) Bill Gates \n B) Steve Jobs \n C) Alan Turing \n D) Charles Babbage \n Your answer:  ")
    if first.upper() == "D":
        print("You won 1 lakh!!!")
        y = input(
            "Now do you want to continue this game or exit with the prize money? \n write yes or no: ")
        if y.lower() == "yes" or y.lower == "y":
            second = input(
                'your question for next round is\n What does the acronym "CPU" stand for in computer terminology?\n A) 1989 \n B) 1991 \n C) 1995 \n D) 1998\n Your Answer: ')
            if second.upper() == "A":
                print("congratulations you won 3lakhs \n Thank u for playing this game")
            else:
                print("Please don't lose hope, try your luck next time")
        else:
            print("You exit the game with total of 1 lakhs!!!")
    else:
        print("THe answer is D charles Babbage. Thank u for playing this game")
else:
    print("You left the game")
