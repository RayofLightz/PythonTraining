def sayWow():
    print("WOW")

def main():
    a = 0 
    while a <= 5:
        print(a)
        sayWow()
        a += 1
    for i in range(0,6):
        print(i)
        sayWow()

if __name__ == "__main__":
    main()
