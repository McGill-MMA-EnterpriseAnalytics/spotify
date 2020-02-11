#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:18:23 2019

@author: luismiguel
"""

from sklearn.linear_model import LogisticRegression
import pandas
from sklearn.model_selection import train_test_split
from sklearn import metrics

##########
## EX1

cancer = pandas.read_csv("/Users/luismiguel/Desktop/McGill MMA/Data Mining/Cancer.csv")
X = cancer.iloc[:,0:9]
y = cancer["class"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 5)
lr = LogisticRegression()
model = lr.fit(X_train, y_train)
y_test_pred = lr.predict(X_test)
print(metrics.accuracy_score(y_test, y_test_pred))

##########
## EX2
X2 = cancer[['clump_thickness', 'bare_nuclei', 'mitoses']]
y2 = cancer["class"]
X2_train, X2_test, y2_train, y2_test = train_test_split(X2,y2, test_size = 0.3, random_state = 5)
lr2 = LogisticRegression()
model2 = lr2.fit(X2_train, y2_train)
y_test_pred2 = lr2.predict(X2_test)
print(metrics.accuracy_score(y2_test, y_test_pred2))

lr2.predict([[2,2,2]])