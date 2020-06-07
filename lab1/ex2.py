tupleList1=[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib', 'Rebeka'),
            ('parent', 'Rakib', 'Sohel'),('parent', 'Hasib', 'Rima'),
            ('parent', 'Hasib', 'Rahim'), ('parent', 'Rashid', 'Hasib')]

tupleList2=["Hasib", "Rakib","Rashid","Sohel","Rahim"]
tupleList3 =["Rebeka","Rima"]

# Procedure to find the Brother of X

X=str(input("Brother of:"))
print('Brother name:', end=' ')
i=0
while(i<=3):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(4):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1])):
                if(tupleList1[i][2] != tupleList1[j][2]):
                    for g in range (5):
                        if(tupleList1[j][2] == tupleList2[g]):
                            print(tupleList1[j][2], end=' ')      
    i=i+1

print(end='\n')

# Procedure to find the Sister of X

X=str(input("Sister of:"))
print('Sister name:', end=' ')
i=0
while(i<=3):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(4):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1])):
                if(tupleList1[i][2] != tupleList1[j][2]):
                    for g in range (2):
                        if(tupleList1[j][2] == tupleList3[g]):
                            print(tupleList1[j][2], end=' ')   
    i=i+1

print(end='\n')

# Procedure to find the Aunt of X

X=str(input("Aunt of:"))
print('Aunt name:', end=' ')
i=0

while(i<=3):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(4):
            for k in range(4): 
                if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][2])):
                    if(tupleList1[j][1] == tupleList1[k][1]):
                        if((tupleList1[j][2] != tupleList1[k][2])):
                            for g in range (2):
                                if(tupleList1[k][2] == tupleList3[g]):
                                    print(tupleList1[k][2], end=' ')
    i=i+1

print(end='\n')

# Procedure to find the Uncle of X

X=str(input("Uncle of:"))
print('Uncle name:', end=' ')
i=0
while(i<=3):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(4):
            for k in range(4):
                if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][2])):
                    if(tupleList1[j][1] == tupleList1[k][1]):
                        if((tupleList1[j][2] != tupleList1[k][2])):
                            for g in range (5):
                                if(tupleList1[k][2] == tupleList2[g]):
                                    print(tupleList1[k][2], end=' ')
    i=i+1
