def sum(n,i,f):
    if(n == 0):
         return 0
    elif(n >= 1):
        return sum(n-1,i,f)+f+(n-1)*i

#main
fterm = int(input('First Term:'))
numterm = int(input('Number of terms:'))
inte = int(input('Interval:'))
total = sum(numterm,fterm,inte)

print('Sum: ', total)
