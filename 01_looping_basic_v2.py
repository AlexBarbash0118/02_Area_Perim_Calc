valid = False
while not valid:

    error = "Please enter a number that is more than zero"

    try:

        response = float(input("Enter a number: "))

        if response > 0: 
            valid = True

        else:
            print("Please enter a number that is more than zero")
            print()   
    
    except ValueError:
        print(error)
