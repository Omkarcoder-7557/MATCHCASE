print("*" * 50)
print("c. Celsius")
print("f. Fahrenheit")
print("k. Kelvin")
print("*" * 50)

ch = input("Enter choice: ")

match ch:

    case "c" | "C":
        c = float(input("Enter temperature in Celsius: "))

        f = (c * 9 / 5) + 32
        k = c + 273.15

        print("Fahrenheit =", f)
        print("Kelvin =", k)

    case "f" | "F":
        f = float(input("Enter temperature in Fahrenheit: "))

        c = (f - 32) * 5 / 9
        k = c + 273.15

        print("Celsius =", c)
        print("Kelvin =", k)

    case "k" | "K":
        k = float(input("Enter temperature in Kelvin: "))

        c = k - 273.15
        f = (c * 9 / 5) + 32

        print("Celsius =", c)
        print("Fahrenheit =", f)

    case _:
        print("Enter valid choice")

print("*" * 50)