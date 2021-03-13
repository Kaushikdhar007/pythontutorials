while(True):
    print("Welcome to our calculator")
    print("Choose + for addition _ for substraction * for multiplication / for division % for percentile ** for power")
    print("Enter your first number")
    var1 = int(input())
    print("Enter your second number")
    var2 = int(input())
    print("Enter what operation you want to do")
    var3 = input()

    if var1 == 46 and var2 == 9 and var3 == '+':
        print("Answer is 72")
    if var1 == 27 and var2 == 10 and var3 == '*':
        print("Answer is 120")
    if var1 == 98 and var2 == 6 and var3 == '/':
        print("Answer is 21")
    if var1 == 956 and var2 == 56 and var3 == '%':
        print("Answer is 535.36")
    if var1 == 5 and var2 == 3 and var3 == '**':
        print("Answer is 125")
    if var1 == 46 and var2 == 28 and var3 == '-':
        print("Answer is 18")

    i = input(("If you want to do more operations then press'y' else 'n'"))
    if i == "y":

        print("Welcome to our calculator")
        print(
            "Choose + for addition _ for substraction * for multiplication / for division % for percentile ** for power")
        print("Enter your first number")
        var1 = int(input())
        print("Enter your second number")
        var2 = int(input())
        print("Enter what operation you want to do")
        var3 = input()

        if var1 == 46 and var2 == 9 and var3 == '+':
            print("Answer is 72")
        if var1 == 27 and var2 == 10 and var3 == '*':
            print("Answer is 120")
        if var1 == 98 and var2 == 6 and var3 == '/':
            print("Answer is 21")
        if var1 == 956 and var2 == 56 and var3 == '%':
            print("Answer is 535.36")
        if var1 == 5 and var2 == 3 and var3 == '**':
            print("Answer is 125")
        if var1 == 46 and var2 == 28 and var3 == '-':
            print("Answer is 18")
        print("If you want to do more operations then press'y' else 'n'\n")
        given = input()
        continue


    else:
        print("Bye")
        break