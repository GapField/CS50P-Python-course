def main():
    something = input("Input: ")
    
    end = check_vowels(something)
    print(end)
def check_vowels(bet):
    result = ""
    vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    for letter in bet:
        if letter not in vowels:
            result += letter
        else:
            result = result    
    return result        

main()
