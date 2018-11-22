from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

names = ["sepal_lenght","sepal_width","petal_length","petal_width","class"]

df = pd.read_table("iris.data",header=None,names=names,sep=",")


X = np.array(df.ix[:,0:4])
y = np.array(df["class"])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)

clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train,y_train)
pred = clf.predict(X_test)

accuracy = accuracy_score(y_test,pred)
print("Predicted model accuracy : "+ str(accuracy))