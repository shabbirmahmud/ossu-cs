def main():
    time = input("What time is it? ")
    timeInt = convert(time)
    if(7<=timeInt<=8):
        print("breakfast time")
    elif(12<=timeInt<=13):
        print("lunch time")
    elif(18<=timeInt<=19):
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    timeInt = hours+minutes/60
    return timeInt

if __name__ == "__main__":
    main()