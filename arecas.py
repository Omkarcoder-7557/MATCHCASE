print("*" * 50)
print("s. Square")
print("r. Rectangle")
print("c. Circle")
print("t. Triangle")
print("*" * 50)

ch = input("Enter choice: ")

match ch:

    case "s" | "S":
        side = float(input("Enter side: "))
        area = side * side
        print("Area of Square =", area)

    case "r" | "R":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of Rectangle =", area)

    case "c" | "C":
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of Circle =", area)

    case "t" | "T":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of Triangle =", area)

    case _:
        print("Enter valid choice")