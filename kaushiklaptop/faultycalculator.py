while(True):
    print("Welcome to our calculator")
    print("Choose + for addition _ for substraction * for multiplication / for division % for percentile ** for power")
    print("Enter your first number")
    var1 = int(input())
    print("Enter your second number")
    var2 = int(input())
    print("Enter what operation you want to do")
    var3 = input()
#addition
    if var1 == 46 and var2 == 9 and var3 == '+':
        print("Answer is 72")
    elif var1!=46 and (var2>=9 or var2<=9) and var3=='+':
        print("Answer is ",var1+var2)
    elif (var1<=46 or var1>=46) and var2!=9 and var3=='+':
        print("Answer is ",var1+var2)

#multiplication
    if var1 == 27 and var2 == 10 and var3 == '*':
        print("Answer is 120")
    elif var1!=27 and (var2>=10 or var2<=10) and var3=='*':
        print("Answer is ",var1*var2)
    elif (var1>=27 or var1<=27) and var2!=10 and var3=='*':
        print("Answer is ",var1*var2)

#division
    if var1 == 98 and var2 == 6 and var3 == '/':
        print("Answer is 21")
    elif var1!=98 and (var2>=6 or var2<=6) and var3=='/':
        print("Answer is ",var1/var2)
    elif (var1>=98 or var1<=98) and var2!=6 and var3=='/':
        print("Answer is ",var1/var2)

#remainder
    if var1 == 956 and var2 == 56 and var3 == '%':
        print("Answer is 535.36")
    elif var1!=956 and (var2>=56 or var2<=56) and var3=='%':
        print("Answer is ",var1%var2)
    elif (var1>=956 or var1<=956) and var2!=56 and var3=='%':
        print("Answer is ",var1%var2)
#power
    if var1 == 5 and var2 == 3 and var3 == '**':
        print("Answer is 125")
    elif var1!=5 and (var2>=3 or var2<=3) and var3=='**':
        print("Answer is ",var1**var2)
    elif (var1>=5 or var1<=5) and var2!=3 and var3=='**':
        print("Answer is ",var1**var2)
#substraction
    if var1 == 46 and var2 == 28 and var3 == '-':
        print("Answer is 18")
    elif var1!=46 and (var2>=28 or var2<=28) and var3=='-':
        print("Answer is ",var1-var2)
    elif (var1>=46 or var1<=46) and var2!=28 and var3=='-':
        print("Answer is ",var1-var2)


    i = input(("If you want to do more operations then press'y' else 'n' \n"))
    if i == "y":

        continue


    else:
        print("Bye\n"
              "Thanks for using our calculator!!")
        break