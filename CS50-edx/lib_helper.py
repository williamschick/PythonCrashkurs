def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

print(f"callee: {__name__}")

if __name__ == "__main__":
    main()