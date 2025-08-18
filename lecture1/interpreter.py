expression = input("Expression: ").split()

if len(expression) != 3: 
    print("invalid format, please use operator")
else:
    try:
        a = int(expression[0])    
        b = int(expression[2])

        match expression[1]:
            case "+":
                print(result = a + b)
            case "-":
                print(result = a - b)
            case "*":
                print(result = a * b)
            case "/":
                print(result = a / b)
            case _:
                print("invalid input")            

    except ValueError:
        print("Invalid number input")
    except ZeroDivisionError:
        print("Error: division by zero")