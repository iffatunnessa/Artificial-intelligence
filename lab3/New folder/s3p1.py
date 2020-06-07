# Writing to and reading from a file in Python
f1=open('stdfile.py', "w")
print("\n")
for i in range(2):
        name=str(input("Enter the name:"))
        dept=str(input("Enter the department:"))
        cgpa=str(input("Enter the cgpa:"))
        std=name+"\t"+dept+"\t"+cgpa
        print(std, end="\n", file=f1)
        
f1.close

f1=open('stdfile.py', "r")       
for l in f1:
        name, dept, cgpa =l.split("\t")
        print(name, dept, float(cgpa), end="\n")
f1.close

# Including files 

import  s3Module1  as  m1

m1.display_file_lines('stdfile.py',2)

n=m1.num_of_lines('stdfile.py')
print("Number of lines in {} is {}.".format('stdfile.py',n))

m1.display_file('stdfile.py')

