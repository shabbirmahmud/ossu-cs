def main():
    inp=input("Write a sentence or something = ")
    print(playback(inp))


def playback(to):
    return to.replace(" ","...")

main()