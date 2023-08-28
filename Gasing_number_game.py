# Gassing the number Game using random module
import random
print("************************************ WALCOME TO THE GAME *********************************")
name = input("Enter your name: ")
while True:
    Ccount = 0
    Ucount = 0
    ch = int(input('''

    1> START
    2> EXIT

    Enter your choise: 

    '''))

    if ch == 1:
        for i in range(1, 11):
            Cnumber = random.randrange(1, 100)
            n = int(input("Enter your number Betbeen 0 To 100 :- "))
            if n > Cnumber:
                print("Computer Number ", Cnumber)
                Ucount = Ucount+1
            elif n < Cnumber:
                print("Computer Number ", Cnumber)
                Ccount = Ccount+1
            elif n == Cnumber:
                print("Computer Number ", Cnumber)
        if Ccount == Ucount:
            print(" Match is Drow")
            print("your Count ",Ucount)
            print("Computer Count ",Ccount)
        elif Ccount < Ucount:
            print("You  Win")
            print("your Count ",Ucount)
            print("Computer Count ",Ccount)
        else:
            print("Computer win")
            print("your Count ",Ucount)
            print("Computer Count ",Ccount)
    else:
        print("Game Over")
        break
    user = input("""
                    y: play again
                    n: No
                     
                    """)
    if user == 'y':
        ch == 1
    else:
        print("Thank You For Match")
        break
