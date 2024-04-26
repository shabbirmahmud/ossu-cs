def main():
    x=float(input("First= "))
    y=float(input("Second= "))
    z=round(x+y)
    print(f"{z:,}")
    z=round(x/y,2)
    print(f"{z}")
    z=x/y
    print(f"{z:.2f}")
    print("First squared is =",int(square(x)))

def square(n):
    return n*n

main()