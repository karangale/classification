import numpy as np
from sklearn import neighbors
from sklearn import cross_validation
import sys

# Load the training data into lists
f = open("train_data.txt")
f1 = open("train_label.txt")
data =  np.loadtxt(fname = f, delimiter = ',')
data1 = np.loadtxt(fname=f1,delimiter=',')
X = data[:,0:]  # select columns 1 through end
y = data1[0:]

# Load the test data into list
f3 = open("test_data.txt")
test = np.loadtxt(fname = f3, delimiter = ',')
T = test[:,0:]

# Split the data for cross validation
X_train, X_test, y_train, y_test=cross_validation.train_test_split(X,y,test_size=0.25,random_state=0)

# Build the model
for weights in ['uniform','distance']:
    nbrs = neighbors.KNeighborsClassifier(algorithm="ball_tree",n_neighbors=15, weights=weights)
    nbrs.fit(X_train,y_train)

# Print the accuracy of the model
print 'Accuracy: ', nbrs.score(X_test,y_test)*100

# Print the predicted  labels of the test data into a file
sys.stdout=open("test_label_kNN.txt","w")

# Predict the labels of the test data
a=nbrs.predict(T)
for elem in a:
    print int(elem) 
