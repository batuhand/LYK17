from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

renkler = ["R","G","B","class"]

df = pd.read_table("Skin_NonSkin.txt",header=None,names=renkler,sep="\t")


X = np.array(df.ix[:,0:3])
y = np.array(df["class"])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.11,random_state=10)

clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train,y_train)
pred = clf.predict(X_test)

accuracy = accuracy_score(y_test,pred)
print("Predicted model accuracy : "/bin + str(accuracy))