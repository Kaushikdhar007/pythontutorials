k=open("kaushik.txt")
#content = k.read() # used to read file whatever you have chosen
#print(content)


#print(k.readline(),end=" ")   #used to print only one line from whatever file you have chosen
#print(k.readline(),end=" ")
#print(k.readline(),end=" ")
#print(k.readline(),end=" ")

print(k.readlines(),end=" ")   #used to print the lines from the file whatever you have chosen as a list
k.close()