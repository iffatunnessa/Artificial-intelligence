# Writing to and reading from a file in Python
f1=open('stdfile.py', "w")
print("\n")       
for i in range(3):
        name=str(input("Enter the name:"))
        dept=str(input("Enter the department:"))
        cgpa=str(input("Enter the cgpa:"))
        std=name+"\t"+dept+"\t"+cgpa
        print(std, end="\n", file=f1)
        print("\n")
f1.close

f1=open('stdfile.py', "r")       
for l in f1:
        name, dept, cgpa =l.split("\t")
        print(name, dept, float(cgpa), end="\n")
f1.close





