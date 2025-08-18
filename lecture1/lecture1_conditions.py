#ifelse statements


'''
#pythonic
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Its an even number")
    else:
        print("Its an odd number")

def is_even(n):
    if n%2 == 0 :
        return True
    else:
        return False
main()
'''
#match
name = "Howard"

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case _:
        print("what 7 are u")    
