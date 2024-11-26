def main():
    filename = input("File name: ").lower().strip()
    fileMediatype(filename)

def fileMediatype(filename):
    ext1=".gif"
    ext2=".jpg"
    ext3=".png"
    ext4=".pdf"
    ext5=".txt"
    ext6=".zip"
    ext7=".jpeg"
    if filename.endswith(ext1):
        print("image/gif")
    elif filename.endswith(ext2):
        print("image/jpeg")
    elif filename.endswith(ext3):
        print("image/png")
    elif filename.endswith(ext4):
        print("application/pdf")
    elif filename.endswith(ext5):
        print("text/plain")
    elif filename.endswith(ext6):
        print("application/zip")
    elif filename.endswith(ext7):
        print("image/jpeg")
    else:
        print("application/octet-stream")

main()