print("WELCOME!!!! To the Snake Water Gun game\n")
i=1
while(i<=10):
    import random

    random_commit = random.choice(["Snake", "Water", "Gun"])
    print("What doo you want to choose \n"
          "Press 'S' for Snake, 'W' for Water, 'G' for Gun\n")
    take=str(input()).capitalize()
    if take=='S' and random_commit== 'Snake':
        print("Tie!!\n On the step",i)
        i = i + 1
    elif take=='S' and random_commit== 'Water':
        print("Win!!\n On the step",i)
        from emoji import emojize

        print(emojize(":kissing_cat:"))
        i = i + 1
    elif take=='S' and random_commit== 'Gun':
        print("Lose!!\n On the step",i)
        i = i + 1
    if take == 'G' and random_commit == 'Snake':
        print("Win!!\n On the step", i)
        from emoji import emojize

        print(emojize(":kissing_cat:"))
        i = i + 1
    elif take == 'G' and random_commit == 'Water':
        print("Lose!!\n On the step", i)
        i = i + 1
    elif take == 'G' and random_commit == 'Gun':
        print("Tie!!\n On the step", i)
        i = i + 1
    if take == 'W' and random_commit == 'Snake':
        print("Lose!!\n On the step", i)
        i = i + 1
    elif take == 'W' and random_commit == 'Water':
        print("Tie!!\n On the step", i)
        i = i + 1
    elif take == 'W' and random_commit == 'Gun':
        print("win!!\n On the step", i)
        from emoji import emojize

        print(emojize(":kissing_cat:"))
        i = i + 1
        continue