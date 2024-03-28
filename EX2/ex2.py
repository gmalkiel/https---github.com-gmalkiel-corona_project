def main():
    print("Choose 1- for a rectangular tower, 2- for a triangular tower, and 3 to exit the program:")
    choice = input()
    # User choice management.
    while choice != '3':
        if choice == '3':
            print("The system closes")
            return
        if choice != '1' and choice != '2':
            print("Invalid input please try again.")
        else:
            print("Enter the height and width of the tower: (syntax: height,width)")
            data = input().split(',')
            if choice == '1':
                action_1(data)
            else:
                action_2(data)
        print("Choose 1- for a rectangular tower, 2- for a triangular tower, and 3 to exit the program:")
        choice = input()


# A function that handles the selection of 1- a rectangular tower.
def action_1(data):
    height = int(data[0])
    width = int(data[1])
    # Check the absolute value of the difference in height and width of the tower.
    # Returning the if the result is greater than 5, otherwise returning the circumference.
    if abs(height - width) > 5:
        print("The area of the tower is:" + str(height * width))
    else:
        print("The perimeter of the tower is:" + str(2 * (height + width)))


# A function that handles the selection of 2- triangular tower.
def action_2(data):
    height = int(data[0])
    width = int(data[1])
    print("Choose option 1 to print the perimeter of the triangle, and option 2 to print the triangle.")
    choice = input()
    if choice == '1':
        triangle_p = triangle_perimeter(width, height)
        print("The perimeter of the tower is:" + str(triangle_p))
        return
    else:
        if width % 2 == 0 or width > 2 * height:
            print("The desired triangle cannot be printed")
        else:
            # Print the first line.
            for i in range(width // 2):
                print(" ", end="")
            print("*")
            num_group = (width - 2) // 2
            if num_group == 0:
                rest = height - 2
            else:
                num_rows = (height - 2) // num_group
                rest = ((height - 2) % num_group)
            # Print remaining lines.
            for i in range(rest):
                for j in range(int((width - 3) / 2)):
                    print(" ", end="")
                for j in range(3):
                    print("*", end="")
                print()
            counter = 3
            # Printing the middle lines.
            for i in range(num_group):
                for j in range(num_rows):
                    for k in range(int((width - counter - (2 * i)) / 2)):
                        print(" ", end="")
                    for k in range(counter + (2 * i)):
                        print("*", end="")
                    print()
            # Print the last line.
            for i in range(width):
                print("*", end="")
            print()
            return


# A function to calculate the perimeter of a triangle by height and base.
def triangle_perimeter(base, height):
    # Calculating the sides of a triangle by the Pythagorean theorem.
    sides = (height ** 2 + (base / 2) ** 2) ** 0.5
    return base + (sides * 2)


if __name__ == "__main__":
    main()