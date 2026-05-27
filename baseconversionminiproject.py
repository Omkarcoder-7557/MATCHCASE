s="""-----------------------------------------------------------------------------------------------
	Base Conversion Calculator
-----------------------------------------------------------------------------------------------
		 1.Decimal  to Binary
 	     2. Decimal to Octal
         3.Decimal to Hexadecimal
		 4.binary to Decimal
		 5.Binary to Octal
		 6.Binary to Hexadecimal
	     7.Octal to Decimal
		 8.Octal to B Binary
         9.Octal to HexaDecimal
		 10.HexaDecimal to Decimal
         11.HexaDecimal to B Binary
         12.HexaDecimal to Octal
-----------------------------------------------------------------------------------------------
"""
print(s)
print("*" * 50)
ch=int(input("Enter your choice: "))

match (ch):
    case 1|2|3:
        n=int(input("enter a decimal number:"))
        bv=bin(n)
        ov=oct(n)
        hv=hex(n)
        print("bin({})={}".format(n,bv))
        print("oct({})={}".format(n,ov))
        print("hex({})={}".format(n,hv))
    case 4|5|6:
        n=input("enter a binary number with 0b:")
        dv=int(n,2)
        ov=oct(int(n,2))
        hv=hex(int(n,2))
        print("decimal({})={}".format(n,dv))
        print("oct({})={}".format(n,ov))
        print("hex({})={}".format(n,hv))
    case 7|8|9:
        n=input("enter a octal number with 0o:")
        dv=int(n,8)
        bv=bin(int(n,8))
        hv=hex(int(n,8))
        print("decimal({})={}".format(n,dv))
        print("bin({})={}".format(n,bv))
        print("hex({})={}".format(n,hv))
    case 10|11|12:
        n=input("enter a hexadecimal number with 0x:")
        dv=int(n,16)
        bv=bin(int(n,16))
        ov=oct(int(n,16))
        print("decimal({})={}".format(n,dv))
        print("bin({})={}".format(n,bv))
        print("oct({})={}".format(n,ov))
print("*" * 50)