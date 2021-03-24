def exargs(normal,*val,**list):
    print("\n In this list the name of the players are:\n")
    for i in val:
        print(i)
    print(normal)
    for key,value in list.items():
        print(f"{key} scores {value}")
talika=["Sachin", "Raina","Kohli","Dhoni","Kaushik","Pathan","Sayan","Smith","Bapi","Krish" ]
normal = "\nThis is the score board of cricket players\n"
run={"Sachin": 200, "Raina":98,"Kohli": 40,"Dhoni": 77,"Kaushik":210,"Pathan": 1200,"Sayan": 20,"Smith": 240,"Bapi": 0,"Krish": 88 }
exargs(normal,*talika, **run)