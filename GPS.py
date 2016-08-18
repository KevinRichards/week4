gopher_number = 1000

import random

for year in range(1,11):
    birth = gopher_number*random.uniform(0.1, 0.2)
    die = gopher_number*random.uniform(0.05, 0.25)
    gopher_number += birth - die
    print("Year {}".format(year))
    print("******")
    print("{:.2f} gophers were born. {:.2f} died.".format(birth,die))
    print("Population: {:.2f}".format(gopher_number))
    print("              ")




