D={'Mayukh':'2016', "Kaushik":'2000', "Soma":'1972', "Rahul":'2001'}
while(True):
    print("Enter the name")
    name=input().capitalize() #whatever input will be given it automatically turns that into capital letter
    print(D[name])
    print("Do you want to search another name if want to then press y else press N\n")
    cond=input().capitalize()
    if cond== "Y":
        continue
    elif cond=="N":
        print("Thanks for using our dictionary")
        break