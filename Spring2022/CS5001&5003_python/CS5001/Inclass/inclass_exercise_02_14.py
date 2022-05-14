def enter():
    user_input = str(input("Enter yes or no: \n"))
    while user_input != 'yes' or user_input != 'no':
        print("Only yes or No will work here")
        user_input = str(input("Please enter yes or no: \n"))

def value_in_a_range():
    number = float(input("Enter a number between 0 and 1: \n"))
    while number < 0 or number > 1:
        print("Enter only a number between 0 and 1")
        number = float(input("Enter a number between 0 and 1: \n"))

def num():
    x = 5
    while x > 0:
        print(x)
        x -= 1
    print("Blastoff")

def is_prime():
    max_value = int(input('Display primes up to what value? '))
    value = 2  # Smallest prime number
    while value <= max_value:
     # See if value is prime
         is_prime = True  # Provisionally, value is prime
     # Try all possible factors from 2 to value - 1
         trial_factor = 2
         while trial_factor < value:
             if value % trial_factor == 0:
                 is_prime = False
                 break
             trial_factor += 1
         if is_prime:
# Found a factor
# No need to continue; it is NOT prime
# Try the next potential factor
             print(value, end= ' ')  # Display the prime number
         value += 1                  # Try the next potential prime number
    print() # Move cursor down to next line

def main():
    is_prime()





if __name__ == '__main__':
    main()
