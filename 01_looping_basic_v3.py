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
width = num_check("Width: ")
height = num_check("Height: ")
print()
print("Width", width)
print("Height", height)
print()
