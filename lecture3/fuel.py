def main():
    result = get_int()
    print(f"result = {result} %")

def get_int():
    while True:
        try:
            fuel = input("Enter the fuel Fraction: ").strip().split("/")
            nenner =int(fuel[0])
            zaehler =int(fuel[1])
            result = int((nenner / zaehler)*100)
            return result                 
        except ValueError:
            pass        
        except ZeroDivisionError:        
            pass           
main()