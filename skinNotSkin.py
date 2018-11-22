from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

renkler = ["R","G","B","class"]

df = pd.read_table("iris.data",header=None,names=names,sep="\t")