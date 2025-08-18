import re

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date()
            break
        except ValueError:
            print("Value Error")
            pass
        except IndexError:
            print("Index Error")
            pass

def date():
    date = input("Date: ").strip()
    date = re.split(r"[ /]+", date)
    x = date[0]
    day = int(date[1])
    if not x.isdigit():
        for i in range(len(month)):
            if x == month[i]:
                monat= i+1
                break
        else:
            raise ValueError("Invalid month name")
    else:
        monat = int(x)

    if not (1 <= day <= 31):
        raise ValueError("Day out of range")
    if not (1 <= monat<= 12):
        raise ValueError("Month out of range")         
                   
    print(f"{date[2]} - {monat:02} - {day:02}")

main()