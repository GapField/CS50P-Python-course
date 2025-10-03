from pathlib import Path
'''
file_path = Path(input("Enter file name: "))

print(file_path.name)     # example.TXT
print(file_path.stem)     # example
print(file_path.suffix)   # .TXT
print(file_path.suffix.lower())  # .txt
print(file_path.exists()) # True if file exists

match file_path.suffix.lower():
    case ".txt" :
        print("text file")
    case ".gif":
        print("GIF File")
    case ".jpg":
        print("jpg File")
    case ".jpeg":
        print("jpeg File")
    case ".png":
        print("PNG File")
    case ".pdf":
        print("pdf File")
    case ".zip":
        print("zip File")
    case _:
        print("application/octet-stream")

'''
text = "hi.jpg"
match text:
    case t if text.endswith("jpg"):
        print("its jpg file")
    case _:
        print("what is this")