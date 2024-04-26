def main():
    name=input("What's your name? ")
    match name:
        case "Omar" | "Rifat" | "Sajjad":
            print("SirajGonj")
        case "Shabbir":
            print("Pirojpur")
        case _:
            print("Who?")
main()