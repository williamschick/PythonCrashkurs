msg = "https://Hello World!                "
msgWithHochKomma = 'This is also a string in \n\'Python\''
msg = msg.strip()
print("Hello World & " + msg + " " + msgWithHochKomma.title())
print("Hello World & " + msg.removeprefix("https://").upper() + " " + msgWithHochKomma.title())

first_name = "william"
last_name = "Schick"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

# this is not possible x, y, z = 0 
x, y, z = 0, 0, 0

print(f"{x} + {y} + {z}")