def main():
    c = 300000000**2

    while True:
        try:
            m = int(input("enter a number "))
            e = m*c
            print(e)

            break
        except ValueError:
            print("Please enter only number")
            
main()
