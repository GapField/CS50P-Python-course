'''
for i in [0, 1, 2]:
    print("meow")

for i in range(3):
    print("meow")

for _ in range(3):
    print("meow")
print("meow"*3)

print("meow\n" * 3, end="")

while True:
    n=int(input("Whats n? "))
    if n < 0: 
        continue
    else:
        break
'''

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)
    
main()
