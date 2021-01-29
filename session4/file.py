def main():
    fd = open("cats.txt", "w+")
    fd.write("mittens\n")
    fd.write("fluffy\n")
    fd.close()
    fd = open("cats.txt", "r")
    filestring = fd.read()
    print(filestring)
    fd.close()

if __name__ == "__main__":
    main()

