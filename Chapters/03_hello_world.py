msg = ["https://Hello World!                ", " zwei "]

print(f"{msg[0]} + {msg[1]}")

msg.append("drei")
print(f"{msg[0]} + {msg[1]}+ {msg[2]}")

del msg[2]
print(f"{msg[0]} + {msg[1]}")

tmp = msg.pop()
print(tmp)

msg.append(tmp)
print(f"{msg[0]} + {msg[1]}")

msg.sort()
print(f"{msg[0]} + {msg[1]}")
