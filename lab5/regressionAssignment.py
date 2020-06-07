# Import the necessary libraries
import matplotlib.pyplot as plot
import pandas
import numpy as np 

def get_alpha():
    global xTrain,yTrain,x_mean,y_mean
    
    nom = 0
    for i in range(len(xTrain)):
        nom = nom + (xTrain[i] - x_mean) * (yTrain[i] - y_mean) 
        
    denom = 0
    for i in range(len(xTrain)):
        denom = denom + pow((xTrain[i] - x_mean),2)  
        
    return nom/denom

def mean_absolute_error():
    global yTest, predictions
    
    nom = 0
    for i in range(len(yTest)):
        nom = nom + abs(yTest[i] - predictions[i])
        
    return nom/len(yTest)

def mean_squared_error():
    global yTest, predictions
    
    nom = 0
    for i in range(len(yTest)):
        nom = nom + pow((yTest[i] - predictions[i]),2)
        
    return nom/len(yTest)


# Import the dataset
dataset = pandas.read_csv(r'C:\Users\Aspire\Desktop\Session5\Codes\salaryData.csv')


# Differentiate attribute and target columns
x = dataset['YearsExperience'].values
y = dataset['Salary'].values

# Reshaping 
X = x.reshape(len(x),1)
Y = y.reshape(len(y),1)

# Spliting dataset into test and training data
xTrain, yTrain, xTest, yTest, predictions  = ([] for i in range(5)) 
for i in range(int(len(X)*1/3)):
    xTrain.append(X[i])
    yTrain.append(Y[i])

for i in range(int(len(X)*1/3), len(X)):
    xTest.append(X[i])
    yTest.append(Y[i])

# Calculating the mean values and alpha, beta
x_mean =  np.mean(xTrain)
y_mean =  np.mean(yTrain)

alpha = get_alpha()
beta = y_mean - alpha*x_mean

# Prediction on Training data
for i in range(len(xTest)):
    predictions.append( alpha* xTest[i] + beta)

print(np.asarray(predictions).shape)
# Visualization
df = pandas.DataFrame({'Actual': np.asarray(yTest).flatten(), 'Predicted': np.asarray(predictions).flatten()})
print(df)
df1 = df
df1.plot(kind='bar')
plot.show()

# Displaying errors
print('Mean Absolute Error:', mean_absolute_error()) 
print('Mean Squared Error:', mean_squared_error()) 
print('Root Mean Squared Error:', np.sqrt(mean_squared_error()))

