
# Including files 

import  s3Module1  as  m1

m1.display_file_lines("stdfile.py",2)

n=m1.num_of_lines("stdfile.py")
print("Number of lines in {} is {}.".format("stdfile.py",n))

m1.display_file("stdfile.py")
