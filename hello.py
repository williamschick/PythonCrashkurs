def main():
    tmp = input("Who are you? ").strip().title()

    hello(tmp)

def hello(tmp):
    print("\"Hello\", " + tmp)


main()