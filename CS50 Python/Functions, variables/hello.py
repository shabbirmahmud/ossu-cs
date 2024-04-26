print("Hello, world")
#ask user for name, then user input then print name
def main():
    name = input("What is your name?\n").strip()
    name = name.title()
    first, last=name.split(" ")
    hello()
    hello(first)

def hello(to="world"):
    print(f"Hello, {to}")

main()