import inflect

p = inflect.engine()
adieu = "Adieu, adieu to "
names = []

while True:
    try:
        name = input("Name: ")
        if name.strip():
            names.append(name.strip())
    except EOFError:
        break

sentence = p.join(names)

print(f"{adieu}{sentence}")