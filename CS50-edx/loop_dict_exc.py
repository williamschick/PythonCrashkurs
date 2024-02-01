while True: 
    try:
        x = int(input("Give me a number ... "))
        break
    except ValueError:
        print("sorry not a number")

print(f"number {x}")


# try:
#     x = int(input("Give me a number ... "))
#     dict = {'1': x}

#     i = 0
#     while i < 3:
#         print(f"{dict['1']}")
#         i += 1

# except ValueError:
#     print("sorry not a number")
