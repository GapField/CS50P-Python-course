grocery = {}

def main():
    get_grocery()

def get_grocery():
    while True:
        try:
            item = input("Enter grocery: ")
            grocery[item] = grocery.get(item, 0) + 1
        except EOFError:
            print("Your grocery to buy: ")
            for key, value in grocery.items():
                print(f"{key}, {value}")    
            break
main()