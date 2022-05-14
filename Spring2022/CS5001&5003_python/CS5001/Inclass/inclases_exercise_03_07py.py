def main():
    size = int(input("Enter the size of the table: "))

    for row in range(1, size + 1):
        for col in range(1, size + 1):
            product = row*col
            print("{0:4}".format(product), end='')
        print()
        
