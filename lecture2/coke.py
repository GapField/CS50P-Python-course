def main():
    coke_price = 50
    current_amount = 0
    while True:
        inserted_coin = insertcoin()
        current_amount += inserted_coin
        if current_amount < 50:            
            print(f"ammount due {coke_price-current_amount}")
        elif current_amount == 50:
            print("Here is your cola")
            break
        elif current_amount > 50:
            print(f"change owed: {current_amount-coke_price},Here is your cola")
            break        

def insertcoin():
    while True:
        try:
            amount = int(input("insert coin "))
            break
        except ValueError:
            print("only coin integer, try again")            
    return amount
        
main()    