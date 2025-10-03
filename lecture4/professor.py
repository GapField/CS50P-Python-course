import random


def main():
    level = int(get_level())
    generate_integer(level)



def get_level():
    while True:        
        try:
            level =  input("Level: ")
            if not level in ("1","2","3"):
                print("enter level only 1, 2 or 3")
            elif level in ("1","2","3"):
                return level
        except ValueError:
            continue    



def generate_integer(level):
    for i in range(10):
        x = random.choice(range(1,10))
        y = random.choice(range(1,10))
        correct_result = x + y
        n = 0
        while n<3:
            answer = int(input(f"{x} + {y} = "))                   
            if answer != correct_result:
                print("EEE")
                n += 1
            elif answer == correct_result:
                break
        print(f"{x} + {y} = {correct_result}")

if __name__ == "__main__":
    main()