import string

def main():
    camelCase= ask()
    snake_case = checkcamel(camelCase)    
    print(f"snake case: {snake_case}")

def ask():
    text = input("camel case: ")
    return text

def checkcamel(camel):
    result = ""
    for letter in camel:
        if letter in string.ascii_uppercase:
            result += "_" + letter.lower()
        else:
            result += letter           
    return result    

main()