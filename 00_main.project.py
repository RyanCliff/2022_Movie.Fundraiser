# Import statements


# Functions go here

# Not blank function
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)

# Main routine

# Get ticket details

# Get name


name = not_blank("Name: ", "Sorry - this can't be blank")
