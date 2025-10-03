import pyfiglet
import sys

try:
    if len(sys.argv) == 1:
        font = None
    elif len(sys.argv) == 3:
        font = sys.argv[2]
        pyfiglet.figlet_format("test", font=font)
    else:
        sys.exit("invalid input")
        
    text = input("Input: ")
    if font:
        ascii_banner = pyfiglet.figlet_format(text, font= font)
    else:
        ascii_banner = pyfiglet.figlet_format(text)
    print(ascii_banner)            
except pyfiglet.FontNotFound as e:
    print("error:", e)
