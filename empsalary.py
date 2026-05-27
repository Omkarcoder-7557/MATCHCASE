#program for the calculating the employee salary
import sys
emno=int(input("enter the emplyee number:"))
name=input("enter the emplyee name:")
bs=float(input("enter the basic salary:"))
#logic
if bs<=0:
    print("please enter the valid salary")
    sys.exit()
elif (bs>=10000):
    da=(25/100)*bs
    ta=(15/100)*bs
    cca=(2/100)*bs
    hra=(8/100)*bs
    ma=(1/100)*bs
    lic=(2/100)*bs
    gpf=(1.5/100)*bs
elif bs<10000:
    da = (12.5/100) * bs
    ta = (7.5/100) * bs
    cca = (1.5/100) * bs
    hra = (6/100) * bs
    ma = (1/100) * bs
    lic = (2/100) * bs
    gpf = (0.5/100) * bs

netsalary=(da+ta+cca+hra+ma)-(lic+gpf)
#showing
print("the employee name is {}".format(name))
print("the employee no is {}".format(emno))
print("the basic salary is {}".format(bs))
print("*"*50)
print("benifits")
print(da)
print(ta)
print(cca)
print(hra)
print(ma)
print("*"*50)
print("deduction")
print(lic)
print(gpf)
print("*"*50)
print("the total salary of emplayee is {}".format(netsalary))
print("*"*50)