# Initialize dictionary
val={"Sachin": 200, "Raina":98,"Kohli": 40,"Dhoni": 77,"Kaushik":210,"Pathan": 1200,"Sayan": 20,"Smith": 240,"Bapi": 0,"Krish": 88 }
print("what type of running order you want to print\n"
      "For highest order type 'B' and for smallest type 'S'\n")
d=str(input()).capitalize()
if d== 'B':
    from heapq import nlargest

    # Initialize N
    N = 5
    # printing original dictionary
    print("The original dictionary is : " + str(val))
    # N largest values in dictionary
    # Using nlargest
    res = nlargest(N,val, key=val.get )

    # printing result
    #print("The top N value pairs are  " + str(res))
    print("Dictionary with 3 highest values:")
    print("Keys: Values")

    for N in res:
        print(N, ":", val.get(N))
elif d=='S':
    from heapq import nsmallest

    # Initialize N
    N = 5
    # printing original dictionary
    print("The original dictionary is : " + str(val))
    # N largest values in dictionary
    # Using nlargest
    res = nsmallest(N, val, key=val.get)

    # printing result
    #print("The top N value pairs are  " + str(res))
    print("Dictionary with 3 smallest values:")
    print("Keys: Values")

    for N in res:
        print(N, ":", val.get(N))

