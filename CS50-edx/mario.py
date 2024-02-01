def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(h):
    for i in range(h):
        print("#" *  (1+i))

if __name__ == "__main__":
    main()