a=input("Enter Employee Name: ")
b=input("Enter Father Name: ")
c=input("Enter your NIC no.: ")
d=input("Enter Attendence how long you stay here: ")
e=input("Enter your Id:")
f=input("Employee Fix Salary: ")
g=input("Employee Overtime Allowance: ")
##module 1
print("\t\t\t\t\t\t\t MODULE -> 1")
print("1.) Employee ID\t\t\t\t\t\t ",e)
print("2.) Employee Full Name \t\t\t\t\t ",a)
print("3.) Father Name \t\t\t\t\t ",b)
print("4.) NIC No. \t\t\t\t\t\t ",c)
print("5.) Attendence \t\t\t\t\t\t",d)
print("6.) Overtime Allowance \t\t\t\t\t ",g)
##module 2
print()
print("\t\t\t\t\t\t\t MODULE -> 2")
print("Employee Fix Salary \t\t\t\t\t",f)
print("Fix Salary+Overtime Allowance \t\t\t\t",(f+g))
annual=f*12
print("Employee Salary per Anum \t\t\t\t", annual)
allowance=g*12
print("Annually Allowance \t\t\t\t\t",allowance) 
print("Annual Salary with Allowance \t\t\t\t",annual+allowance)
