import random
import sys

number= []
while True:
    try: 
        n = int(input("Level: "))
        if n <1:
            print("Level must be bigger than 1")
            continue
        number = list(range(1, n+1))
        break
    except ValueError:
        continue
    except EOFError:
        print("Game ended.")
        sys.exit()    

answer = random.choice(number)

while True:
    try:
        guess = int(input("Guess "))
        if guess == answer:
            print("Just Right!")
            break
        elif guess > answer:
            print("Too Large")
        elif guess < answer:
            print("Too Small")    
    except EOFError:
        print("game ended")        
        break
    except ValueError:
        print("enter valid number")    
        continue