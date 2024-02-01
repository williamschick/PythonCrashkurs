# sample to import a library from python
import random

def main():
    # random choice method
    x = random.choice(["heads", "tails"])
    print(f"result: {x}")

    # random randint method
    x_int = random.randint(4, 10)
    print(f"result: {x_int}")

    # random shuffle method
    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for card in cards:
        print(f"result: {card}")

if __name__ == "__main__":
    main()