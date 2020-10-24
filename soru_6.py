# This programme returns the numbers that
# first number is greater than last number
count = 0

for i in range(1000,10000):
    if (int(str(i)[0])) > (int(str(i)[-1])):        # First we convert 2 str
        print(i)                                    # 2 reach first digit
        count += 1                                            # then, reconvert that number as int
print(f"There're {count} numbers.")    