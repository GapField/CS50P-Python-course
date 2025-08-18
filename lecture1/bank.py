greeting= input("Greeting: ")

check = greeting.lower().strip().split()
if check[0] == "hello":
    print("$0")
elif check[0][0] == "h": #first bracket [] is word, second is char
    print("$20")
else:
    print("$100")
