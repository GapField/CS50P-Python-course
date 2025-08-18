def main():
    time = input("What time is it? ")
    time = convert(time)
    match time:
        case time if 7 <= time <= 8:
            print("breakfast time")
        case time if 12 <= time <= 13:
            print("lunch time")
        case time if 18 <= time <= 19:
            print("dinner time")

def convert(time):
    time = time.split(":")
    hour = float(time[0])
    min = float(time[1])
    time_float = hour + min/60
    return time_float

if __name__ == "__main__":
    main()