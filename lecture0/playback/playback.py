def main():
    text = input("Enter any word")
    slow_text = "...".join(text.split())
    print(slow_text)
    alt()

def alt():
    text = input("Enter any word")
    slow_text = text.replace(" ", "...")
    print(slow_text)

main()
