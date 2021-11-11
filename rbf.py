#this code is the implementation of rbf to classify Versicolor and Virginica
import q5a
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib.pyplot as plt
desired = np.zeros(100)
data = np.zeros((100,4))
err = []
for i in range(50,150):
    data[i-50][0] = q5a.data_lst[i][0]
    data[i-50][1] = q5a.data_lst[i][1]
    data[i-50][2] = q5a.data_lst[i][2]
    data[i-50][3] = q5a.data_lst[i][3]
    if i<100:
        desired[i-50] = 1
    else:
        desired[i-50] = -1
lst = []
for i in range(100):
    lst.append(i)
np.random.shuffle(lst)
training = []
testing = []
for i in range(70):
    training.append(lst[i])
for i in range(70,100):
    testing.append(lst[i])
#first we compute the k means for the data_lst
clusters = 10 # number of clusters
means = np.random.rand(clusters,4) # initilisation of the means
for i in range(clusters):
    means[i][0] = 6 + np.random.rand()
    means[i][1] = 2.5 +  np.random.rand()
    means[i][2] = 4.2 +  np.random.rand()
    means[i][3] = 1.5 +  np.random.rand()
#print(means)
#means = np.zeros((5,4))
asgn = np.zeros(100)
for c in range(1000):
    # assigns each data point the nearest mean
    for i in lst:
        #print(data[i])
        dist = np.zeros(clusters)
        for j in range(clusters):
            dist[j] = np.linalg.norm(data[i] - means[j])
            #print(dist[j])
        #print(dist)
        asgn[i] = np.argmin(dist)
    #print(asgn)
    #now to update the means
    for i in range(clusters):
        sum = np.zeros(4)
        count = 0
        for j in range(100):
            if asgn[j] == i:
                 sum = sum + data[j]
                 count = count + 1
        if sum[0] + sum[1] + sum[2] + sum[3] != 0:
            means[i] = sum/count
#print("Final")
#print(means)
Dmax = 0
for i in range(clusters):
    for j in range(clusters):
        d = np.linalg.norm(means[i] - means[j])
        if d > Dmax:
            Dmax = d
#Now we implement the rbf network
weights = np.zeros(clusters)
#print(weights)
P = 10**(-3)*np.identity(clusters)
#g = np.zeros((10,1))
alpha = 0
hidden_output = np.zeros(clusters)

for i in training:
    er = 0
    for j in range(clusters):
        hidden_output[j] = np.exp((-0.5/((Dmax/np.sqrt(2*clusters))*(Dmax/np.sqrt(2*clusters)))) * np.linalg.norm(data[i] - means[j]) * np.linalg.norm(data[i] - means[j]))
        #print(hidden_output)
    # now we update the weights, we follow same notation as the book
    denom = 1 + np.dot(np.dot(hidden_output,P),np.transpose(hidden_output))
    P = P - (1/denom)*np.dot(np.dot(P,np.transpose(hidden_output)),np.dot(hidden_output,P))
    #print(P)
    g = np.dot(P,np.transpose(hidden_output))
    #print(g)
    alpha = desired[i] - np.dot(weights,np.transpose(hidden_output))
    #print(alpha)
    weights = weights + g*alpha
    #print(weights)
    # Now to compute error Trajectory
    for p in testing:
        for j in range(clusters):
            hidden_output[j] = np.exp((-0.5/((Dmax/np.sqrt(2*clusters))*(Dmax/np.sqrt(2*clusters)))) * np.linalg.norm(data[p] - means[j]) * np.linalg.norm(data[p] - means[j]))
        predicted = np.dot(weights,np.transpose(hidden_output))
        if predicted > 0 and desired[p]==-1:
            er = er + 1
        if predicted < 0 and desired[p] == +1:
            er = er + 1
    err.append(er*3.333)

#print("Final")
#print(weights)

# now to plot
x_list = []
for i in range(1, 71):
       x_list.append(i)
plt.scatter(x_list,err)
plt.plot(x_list,err)
plt.xlabel("Iteration")
plt.ylabel("%error")
plt.title("Error Trajectory")
plt.show()
