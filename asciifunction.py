LOWER = 33
UPPER = 127


def main():
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character,ord(character)))
    digit = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(digit,chr(digit)))
    for i in range(LOWER, UPPER):
        print("{:5}     {:2}".format(i,chr(i)))

def get_number(lower,upper):
    finished = False
    while not finished:
       try:
           num = int(input("Enter a number ({} - {}):".format(lower, upper)))
           if num < lower or num > upper:
               print("Number must be between {} - {}".format(lower, upper))
           else:
                finished = True
       except ValueError:
            print("Input must be integer")
    return num

main()