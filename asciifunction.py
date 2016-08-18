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




LOWER = 33
upper = 127
character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character,ord(character)))
##digit = int(input("Enter a number ({} - {}):".format(LOWER, upper)))
##while digit<LOWER or digit>upper:
  ##  digit = int(input("Enter a number between {} and {}: ".format(LOWER, upper)))
digit = get_number(LOWER,upper)
print("The character for {} is {}".format(digit,chr(digit)))
for i in range(LOWER, upper):
    print("{:5}     {:2}".format(i,chr(i)))

