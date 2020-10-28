for first_number in range(10,100):
    first_number = str(first_number)
    for second_number in range(10,100):
        second_number = str(second_number)
        if (int(first_number) + int(second_number)) * 11 == int(first_number + second_number):
            print(f"{first_number} and {second_number} are numbers searched.")