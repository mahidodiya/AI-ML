import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv('placement.csv')
#print(df.head())

#scatter plot(visulizing data)
plt.scatter(df['cgpa'],df['package'])
plt.xlabel("CGPA")
plt.ylabel("Package(In lpa)")
#plt.show()

#divieding data into input and output column
x=df.iloc[:,0:1]
y=df.iloc[:,-1]
#print(x)


