#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-08-01 13:02
#@Author: daemon
#@File  : 5.py


from __future__ import print_function
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics

iris = load_iris()
X = iris.data
Y = iris.target


print(Y)

#feature engineering:特征工程是将原始数据转化为特征的过程
poly=PolynomialFeatures(3)
X_poly=poly.fit_transform(X)
print('---------1------------')
print(X)
print('----------2-----------')
print(X_poly)
print('-----------3----------')

X_train,X_test,Y_train, Y_test = train_test_split(X, Y, random_state=4)

#model training
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,Y_train)

#predict
Y_pred=knn.predict(X_test)
print("------------")
print(Y_pred)
print(Y_test)
print(knn.score(X_test, Y_test))

#cross validation
# 交叉验证
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
k_range = range(1, 31)
k_scores = []
for k in k_range:
    print(k)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, Y_train, cv=10, scoring='accuracy') # for classification
    k_scores.append(scores.mean())

plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.savefig('knn.jpg')
plt.show()






