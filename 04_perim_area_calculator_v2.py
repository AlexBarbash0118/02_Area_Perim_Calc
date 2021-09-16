# functions go here

# checks if input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response > 0: 
                return response

            else:
                print("Please enter a number that is more than zero")
                print()   
        
        except ValueError:
            print(error)



# Main routine goes here

# Introduction / Heading print statements
print()
print("**** Area Perimeter Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area (width x height)
    area = width * height

    # Calculate perimeter (width x height) x 2
    perimeter = 2 * (width + height)

    # Output area and perimeter to 2 dp
    print("Perimeter: {:.2f} units".format(perimeter))
    print("Area: {:.2f} square units".format(area))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter caclulator")
