import q5
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib.pyplot as plt
data = np.zeros((100,2))
for i in range(50,150):
    data[i-50][0] = q5.data_lst[i][0]
    data[i-50][1] = q5.data_lst[i][1]
lst = []
for i in range(100):
    lst.append(i)
np.random.shuffle(lst)
#print(lst)
#first we compute the k means for the data_lst
clusters = 5 # number of clusters
#means = np.random.rand(5,2) # initilisation of the means
#means = np.array([[7.5,1],[5,2.5],[5.1,2],[5.2,1.5],[7,1]])
means = np.zeros((5,2))
for i in range(5):
    means[i][0] = 6 + np.random.rand()
    means[i][1] = 2.5 +  np.random.rand()
#print(means)
#means = np.zeros((10,4))
asgn = np.zeros(100)
for c in range(20):
    # assigns each data point the nearest mean
    for i in lst:
        #print(data[i])
        dist = np.zeros(5)
        for j in range(5):
            dist[j] = np.linalg.norm(data[i] - means[j])
            #print(dist[j])
        #print(dist)
        asgn[i] = np.argmin(dist)
    print(dist)
    print(asgn)
    #now to update the means
    for i in range(5):
        sum = np.zeros(2)
        count = 0
        for j in range(100):
            if asgn[j] == i:
                 sum = sum + data[j]
                 count = count + 1
        if sum[0] + sum[1] != 0:
            means[i] = sum/count
print("Final")
print(means)
# for plotting
for i in lst:
    if asgn[i] == 0:
        plt.scatter(data[i][0],data[i][1],color = 'blue')
    elif asgn[i] == 1:
        plt.scatter(data[i][0],data[i][1],color = 'red')
    elif asgn[i] == 2:
        plt.scatter(data[i][0],data[i][1],color = 'green')
    elif asgn[i] == 3:
        plt.scatter(data[i][0],data[i][1],color = 'black')
    else:
        plt.scatter(data[i][0],data[i][1],color = 'brown')

plt.show()
