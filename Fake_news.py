import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import  train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
df = pd.read_csv('news.csv')
df.shape
df.head()
labels= df.label
labels.head()
#Split data
X_train,X_test,y_train,y_test = train_test_split(df['text'],labels,test_size=0.2,random_state=7)
#Intialize
tfidf_vectorizer = TfidfVectorizer(stop_words='english',max_df=0.7)
#Fit and transform
tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test = tfidf_vectorizer.transform(X_test)
#intialize
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)
#predic and calculate accuracy
pred = pac.predict(tfidf_test)
score = accuracy_score(y_test,pred)
print(f'Accuracy: {round(score*100,2)}%')