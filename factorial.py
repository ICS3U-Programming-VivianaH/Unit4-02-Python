#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: april, 2025
# The program allows the user to enter a whole number.
# It then uses a do..while loop to calculate the factorial
# of that number.
def main():
    user_input = input("Enter a number: ")

    try:
        user_num = int(user_input)

        if user_num >= 0:
            product = 1
            counter = 0
            while counter < user_num:
                counter += 1
                product *= counter
            print(f"{user_num}! = {product}")
        else:
            print("Number must be a whole number!")
    except:
        print("user_input is not an integer.")


if __name__ == "__main__":
    main()
