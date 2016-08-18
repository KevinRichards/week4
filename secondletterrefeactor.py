
def main():
    name = get_name()
    letter_order = int(input("Order of letter: "))

    method_name(letter_order, name)

def get_name():
    name = input("Enter your name: ")
    while name == "":
        name = input("Enter your name: ")
    return name

def method_name(letter_order, name):
    for i in range(letter_order - 1, len(name), letter_order):
        print(name[i])

main()

