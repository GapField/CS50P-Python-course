def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if checklength(s) and checkletters(s) and checknumbers(s):
        return True
    else: return False

def checklength(s):
    return 2 <= len(s) <=6

def checkletters(s):
    return s[0:1].isalpha()

def checknumbers(s):
    '''
    number_started = False
    
    for ch in s:
        if ch.isdigit():
            if not number_started:
                number_started = True
                if ch == "0":
                    return False
        else:
            if number_started:
                return False
    return True                
    '''
    number_started = False
    for ch in s[2:]:
        if ch.isdigit():
            if not number_started:
                number_started = True
                if ch == '0':
                    return False
        else:
            if number_started == True:
                return False
    return True

main()
