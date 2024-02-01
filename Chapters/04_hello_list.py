msgs = ["https://Hello World!                ", "zwei ", "drei", "vier"]

for msg in msgs:
    print(msg.upper())
    print(msg.lower())

ints = list(range(0,10))
print(ints)
for i in ints:
    print(i)

squares = [value**2 for value in range(1, 11)]
print(squares)

print(squares[0:3])

for s in squares[:4]:
    print(s)

print("Thanks!")