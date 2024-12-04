with open("2023/day_1/input.txt", "r") as file:
    final_result = 0
    for word in file:
        # Set first int, last int and result back to 0 for the next word.
        firstint = 0
        lastint = 0
        result = 0
        for char in word:
            if char.isdigit() and firstint == 0:
                firstint = char
                lastint = char
            elif char.isdigit() and firstint != 0:
                lastint = char
        result = str(firstint) + str(lastint)
        print(result)
        final_result = final_result + int(result)
    print(final_result)
