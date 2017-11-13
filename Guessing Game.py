import random

def main():
    play = True
    bob = ("Number of guesses: ")
    print("Welcome!")
    print("-------")
    while play == True:
        print("--------------------")
        print("Would you like to play: 1. 1 Player 2. 2 Player 3. Vs Computer")
        print("-------")
        choice = input("Press 1, 2, or 3:")
        if choice == 1:
            print("-------")
            print("1 = easy   2 = medium   3 = hard.")
            print("")
            diff = input("Press 1, 2, or 3:")
            if diff == 1:
                x = random.randrange(1, 11)
                guess = input("Pick a number from 1 to 10:")
                guess = int(guess)
                numg = 1
                while(guess != x):
                    if guess > x:
                        print("Too high")
                    else:
                        print("Too low")
                    numg = numg + 1
                    guess = raw_input("Guess again: ");
                    guess = int(guess)
                print("Congratulations, you got the number.")
                print(bob ,numg)

            elif diff == 2:
                x = random.randrange(1, 21)
                guess = input("Pick a number from 1 to 20:")
                guess = int(guess)
                numg = 1
                while(guess != x):
                    if guess > x:
                        print("Too high")
                    else:
                        print("Too low")
                    numg = numg + 1
                    guess = raw_input("Guess again: ");
                    guess = int(guess)
                print("Congratulations, you got the number.")
                print(bob, numg)

            else:
                x = random.randrange(1, 101)
                guess = input("Pick a number from 1 to 100:")
                guess = int(guess)
                numg = 1
                while(guess != x):
                    if guess > x:
                        print("Too high")
                    else:
                        print("Too low")
                    numg = numg + 1
                    guess = raw_input("Guess again: ");
                    guess = int(guess)
                print("Congratulations, you got the number.")
                print(bob, numg)

#2 Player :)

        elif choice == 2:
            winsone = 0
            winstwo = 0
            print("-------")
            print("1 = easy   2 = medium   3 = hard.")
            print("")
            diff = input("Press 1, 2, or 3:")
            round = 1
            if diff == 1:
                z = 11
            elif diff == 2:
                z = 21
            else:
                z = 101
            while (round < 4):
                print("----------")
                print("Round", round)
                print("----------")
                x = random.randrange(1, z)
                y = random.randrange(1, z)

                numg = 0
                numg_a = 0
                guess_a = 300
                guess = 300
                while(guess != x) or (guess_a != y):

                    if guess != x:
                        print("P1: Pick a number from 1 to", z-1)
                        guess = input("Number:")
                        guess = int(guess)
                        if guess > x:
                            print("Too high")
                            print("")
                            numg = numg + 1
                        elif guess < x:
                            print("Too low")
                            print("")
                            numg = numg + 1
                        else:
                            print("Congratulations, you got the number.")
                            print("")
                            numg = numg + 1
                            if guess_a == y:
                                print("P1 number of guesses:", numg)
                                print("P2 number of guesses:", numg_a)
                                if numg < numg_a:
                                    print("P1 wins Round", round)
                                    round = round + 1
                                    winsone = winsone + 1
                                else:
                                    print("P2 wins Round", round)
                                    round = round + 1
                                    winstwo = winstwo + 1

                    if guess_a != y:
                        print("P2: Pick a number from 1 to", z - 1)
                        guess_a = input("Number:")
                        guess_a = int(guess_a)
                        if guess_a > y:
                            print("Too high")
                            print("")
                            numg_a = numg_a + 1
                        elif guess_a < y:
                            print("Too low")
                            print("")
                            numg_a = numg_a + 1
                        else:
                            print("Congratulations, you got the number.")
                            print("")
                            numg_a = numg_a + 1
                            if guess == x:
                                print("P1 number of guesses:", numg)
                                print("P2 number of guesses:", numg_a)
                                if numg < numg_a:
                                    print("P1 wins Round", round)
                                    round = round + 1
                                    winsone = winsone + 1
                                else:
                                    print("P2 wins Round", round)
                                    round = round + 1
                                    winstwo = winstwo + 1

            if winsone > winstwo:
                print("----------")
                print("P1 wins overall!")
            if winstwo > winsone:
                print("----------")
                print("P2 wins overall!")

#Vs Computer :)
        else:
            winsone = 0
            winstwo = 0
            print("-------")
            print("1 = easy   2 = medium   3 = hard.")
            print("")
            diff = input("Press 1, 2, or 3:")
            round = 1
            if diff == 1:
                z = 11
            elif diff == 2:
                z = 21
            else:
                z = 101
            while (round < 4):
                print("----------")
                print("Round", round)
                print("----------")
                x = random.randrange(1, z)
                y = random.randrange(1, z)

                numg = 0
                numg_a = 0
                guess_a = 300
                guess = 300
                while (guess != x) or (guess_a != y):

                    if guess != x:
                        print("P1: Pick a number from 1 to", z - 1)
                        guess = input("Number:")
                        guess = int(guess)
                        if guess > x:
                            print("Too high")
                            print("")
                            numg = numg + 1
                        elif guess < x:
                            print("Too low")
                            print("")
                            numg = numg + 1
                        else:
                            print("Congratulations, you got the number.")
                            print("")
                            numg = numg + 1
                            if guess_a == y:
                                print("P1 number of guesses:", numg)
                                print("Computer number of guesses:", numg_a)
                                if numg < numg_a:
                                    print("P1 wins Round", round)
                                    round = round + 1
                                    winsone = winsone + 1
                                else:
                                    print("Computer wins Round", round)
                                    round = round + 1
                                    winstwo = winstwo + 1

                    if guess_a != y:
                        print("Computer: Pick a number from 1 to", z - 1)
                        if guess_a == 300:
                            guess_a = (z-1)/2
                            print(guess_a)
                        elif guess_a < y:
                            guess_a = guess_a + guess_a/2 + random.randrange(0,2)
                            # if guess_a > 10:
                            #     guess_a = 10
                            # else:
                            #     guess_a = guess_a
                            print(guess_a)
                        elif guess_a > y and guess_a < 300:
                            guess_a = guess_a/2 + random.randrange(0,2)
                            # if guess_a < 1:
                            #     guess_a = 1
                            # else:
                            #     guess_a = guess_a
                            print(guess_a)

                        if guess_a > y:
                            print("Too high")
                            print("")
                            numg_a = numg_a + 1
                        elif guess_a < y:
                            print("Too low")
                            print("")
                            numg_a = numg_a + 1
                        else:
                            print("Congratulations, you got the number.")
                            print("")
                            numg_a = numg_a + 1
                            if guess == x:
                                print("P1 number of guesses:", numg)
                                print("Computer number of guesses:", numg_a)
                                if numg < numg_a:
                                    print("P1 wins Round", round)
                                    round = round + 1
                                    winsone = winsone + 1
                                else:
                                    print("Computer wins Round", round)
                                    round = round + 1
                                    winstwo = winstwo + 1

            if winsone > winstwo:
                print("----------")
                print("P1 wins overall!")
            if winstwo > winsone:
                print("----------")
                print("Computer wins overall!")


#playagain?
        playagain = input("Would you like to play again? (1 = yes and 2 = no)")
        if playagain == 1:
            play == True
        else:
            break;

    print("--------------------")
    print("Thanks for playing!")
    print("--------------------")
main()