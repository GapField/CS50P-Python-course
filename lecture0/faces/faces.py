def main():
    emoji = {
    ":)" : "🙂",
    ":(" : "🙁"
    }
    text = input("Enter text with :) or :( ")
    for key, value in emoji.items():
        text = text.replace(key,value)
    print(text)
    
main()
