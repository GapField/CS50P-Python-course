menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    get_price()

def get_price():
    result = 0
    while True:
        try:
            food = input("What you want? ").strip().title()      
        except EOFError:
            print(f"Final Price: {result}$")
            break        
        if food in menu:
            result += menu[food]
            print(f"your current price: {result}$") 
            
main()