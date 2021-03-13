n=18
print("You have only 5 guesses!! So please be aware to do the operation\n")
time_of_guessing=1
while(time_of_guessing<=5):

    no_to_guess = int(input("ENTER your number\n"))
    if no_to_guess>n:
        print("You guessed the number above the actual one\n")
        print("You have only", 5 - time_of_guessing, "more guesses")
        time_of_guessing = time_of_guessing + 1
    elif no_to_guess<n:
        print("You guessed the number below the actual one\n")
        print("You have only",5-time_of_guessing,"more guesses")
        time_of_guessing=time_of_guessing+1
        continue
    elif no_to_guess==n:
        print("You have printed the actual number by guessing successfully at guess no.",time_of_guessing)
        break



