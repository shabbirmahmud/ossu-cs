def main():
    inp = input("Greeting: ").lower().strip()
    first = inp.split(" ",1)[0]
    if (first == "hello" or first == "hello,"):
        print("$0")
    elif (first[0] == "h"):
        print("$20")
    else:
        print("$100")

main()