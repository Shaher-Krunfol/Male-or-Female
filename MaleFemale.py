from sklearn import tree

# [height, width, shoe size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [155, 55, 36], [196, 86, 48], [170, 55, 37]]

Y = ['male', 'male', 'female', 'female', 'male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([[200, 88, 50]])

print(prediction)