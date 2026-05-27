#program for the airthmatic calculator using match case
print("*"*50)
print("\t\t\tAIRENTHMATIC OPERATORS CALCULATOR")
print("*"*50)
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
print("6.exponent")
print("*"*50)
ch=int(input("enter your choice:"))
match(ch):
    case 1:
        print("enter two numbers:")
        a,b=int(input()),int(input())
        print("add({},{}={})".format(a,b,a+b))
    case 2:
        print("enter two numbers:")
        a,b=int(input()),int(input())
        print("sub({},{}={})".format(a,b,a-b))
    case 3:
        print("enter two numbers:")
        a, b = int(input()), int(input())
        print("mul({},{}={})".format(a, b, a*b))
    case 4:
        print("enter two numbers:")
        a, b = int(input()), int(input())
        print("div({},{}={})".format(a, b, a/b))
        print("floor division({},{}={})".format(a, b, a//b))
    case 5:
        print("enter two numbers:")
        a, b = int(input()), int(input())
        print("mod({},{}={})".format(a, b, a%b))
    case 6:
        a,b=int(input("enter number")), int(input("enter power"))
        print("pow({},{}={})".format(a, b, a**b))
    case _:
        print("enter valid choice")
print("*"*50)

