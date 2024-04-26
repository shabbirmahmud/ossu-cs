def main():
    inp=input("Enter any text= ")
    print(emoji(inp))

def emoji(of):
    return of.replace(":)", "🙂").replace(":(", "🙁")

main()