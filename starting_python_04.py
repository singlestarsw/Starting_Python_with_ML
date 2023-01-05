#Video: Starting Out With Python with ML 02

#Author: Gentry
#Channel: Single Star Software


#Imports
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

if __name__ == '__main__':

    models = [
        DecisionTreeClassifier(criterion='entropy'),
        KNeighborsClassifier(n_neighbors=3),
        SVC(),
    ]

    #Get our dataset
    X, y = load_wine(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True, random_state=42)

    
    for model in models:
        #Train our model 
        model.fit(X_train, y_train)

        #Test our model on test
        y_pred = model.predict(X_test)
        print('------------', type(model), '------------')
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

    


