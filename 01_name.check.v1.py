
def not_blank(question):
    valid = False

    while not valid:
        try:
            name = input(question)
