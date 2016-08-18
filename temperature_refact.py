MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()


def celsius_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def fahrenheit_celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print("Result: {:.2f} F".format(celsius))


while choice != "Q":
    if choice == "C":
        celsius_fahrenheit()
    elif choice == "F":
        fahrenheit_celsius()

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
