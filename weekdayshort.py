#WRTE A PYTHON PROGRAM WHICH WILL TAKE DAY OF WEEK AND VALIDATE IT IS WORKING DAY WEEK END OR HOLIDAY (USING MATCH CASE)
from unittest import case
wek=input("enter any day:").upper().strip()
match (wek):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is a working day".format(wek))
    case "SATURDAY":
        print("{} is a week end day".format(wek))
    case "SUNDAY":
        print("{} is a holi day".format(wek))
    case _:
        print("{} is not a valid day".format(wek))
print("*"*50)