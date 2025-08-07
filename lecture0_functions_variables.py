#String and Parameters

name = input("What's your name ")
print("hello,", name, sep =' ') #output: hello, howard
print("hello,"+ name, sep =' ') #output: hello,howard separator doesnt apply in here
print("hello, "+ name, end="ddd") # output: hello, howardddd

#Formatting Strings
print("")

# Remove whitespace from the str
name = name.strip() # remove any whitespace ferom the left and right of the user's input
print(f"hello, {name}") #use to combine text and variables, or format numbers or exprfession {x**2}

#Capitalize the first letter of each word
name = name.title() #howard -> Howard

#Efficient Modify
name = name.strip().title()
#or
#name = input("Whats ur name?").strip().title()

#Integers or int
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print(z) # output: 91 because it intepret the input as string
z = int(x) + int(y) # fix it by converting string to integer

#input as string
x = int(input("What's x? "))
y = int(input("What's y? "))
z = x+y
print(z) # or print(x + y)

x = float(input("What's x? float"))
y = float(input("What's y? float"))

# Create a rounded result
z = round(x + y)

# Print the result
print(z)