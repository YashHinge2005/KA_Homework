rollno= eval(input("Enter Rollno of first Student:-"))
name=(input("Enter Name of first Student:-"))
marks= eval(input("Enter Marks of first Student:-"))

rollno2= eval(input("Enter Rollno Second Student:-"))
name2=(input("Enter Name of Second Student:-"))
marks2= eval(input("Enter Marks of Second Student:-"))

print("------------------------------------------------------------------------")
print("|","RollNo".center(20),"|","Name".center(20),"|","Marks".center(20),"|")
print("------------------------------------------------------------------------")
print(f"|{rollno:^22}|{name:^22}|{marks:^22}|")
print(f"|{rollno2:^22}|{name2:^22}|{marks2:^22}|")
print("------------------------------------------------------------------------")


