import q5a
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib.pyplot as plt
'''
# this is the Distortion Plot Versicolor and Virginica
desired = np.zeros(100)
data = np.zeros((100,4))
disto = []
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
#first we compute the k means for the data_lst
#clusters = 10 # number of clusters
for clusters in range(1,21):
    print(clusters)
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
    distortion = 0
    for i in lst:
        k = int(asgn[i])
        distortion = distortion + (np.linalg.norm(means[k] - data[i])*np.linalg.norm(means[k] - data[i]))
    disto.append(distortion)
    #print("Final")
    #print(means)

# now to plot
x_list = []
for i in range(1, 21):
       x_list.append(i)
plt.scatter(x_list,disto)
plt.plot(x_list,disto)
plt.xlabel("Clusters")
plt.ylabel("Distortion")
plt.title("Distortion Plot(Versicolor and Virginica)")
plt.show()
'''
'''
# this is the Distortion Plot Setosa and Virginica
desired = np.zeros(100)
data = np.zeros((100,4))
disto = []
for i in range(50):
    data[i][0] = q5a.data_lst[i][0]
    data[i][1] = q5a.data_lst[i][1]
    data[i][2] = q5a.data_lst[i][2]
    data[i][3] = q5a.data_lst[i][3]
    desired[i] = 1

for i in range(100,150):
    data[i-50][0] = q5a.data_lst[i][0]
    data[i-50][1] = q5a.data_lst[i][1]
    data[i-50][2] = q5a.data_lst[i][2]
    data[i-50][3] = q5a.data_lst[i][3]
    desired[i-50] = -1

lst = []
for i in range(100):
    lst.append(i)
np.random.shuffle(lst)
#first we compute the k means for the data_lst
#clusters = 10 # number of clusters
for clusters in range(1,21):
    print(clusters)
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
    distortion = 0
    for i in lst:
        k = int(asgn[i])
        distortion = distortion + (np.linalg.norm(means[k] - data[i])*np.linalg.norm(means[k] - data[i]))
    disto.append(distortion)
    #print("Final")
    #print(means)

# now to plot
x_list = []
for i in range(1, 21):
       x_list.append(i)
plt.scatter(x_list,disto)
plt.plot(x_list,disto)
plt.xlabel("Clusters")
plt.ylabel("Distortion")
plt.title("Distortion Plot(Setosa and Virginica)")
plt.show()
'''

# this is the Distortion Plot Versicolor and Setosa
desired = np.zeros(100)
data = np.zeros((100,4))
disto = []
for i in range(100):
    data[i][0] = q5a.data_lst[i][0]
    data[i][1] = q5a.data_lst[i][1]
    data[i][2] = q5a.data_lst[i][2]
    data[i][3] = q5a.data_lst[i][3]
    if i<50:
        desired[i] = 1
    else:
        desired[i] = -1
lst = []
for i in range(100):
    lst.append(i)
np.random.shuffle(lst)
#first we compute the k means for the data_lst
#clusters = 10 # number of clusters
for clusters in range(1,21):
    print(clusters)
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
    distortion = 0
    for i in lst:
        k = int(asgn[i])
        distortion = distortion + (np.linalg.norm(means[k] - data[i])*np.linalg.norm(means[k] - data[i]))
    disto.append(distortion)
    #print("Final")
    #print(means)

# now to plot
x_list = []
for i in range(1, 21):
       x_list.append(i)
plt.scatter(x_list,disto)
plt.plot(x_list,disto)
plt.xlabel("Clusters")
plt.ylabel("Distortion")
plt.title("Distortion Plot(Setosa and Versicolor)")
plt.show()

'''
# Now we plot the Misclassification rate varying clusters
error = []
desired = np.zeros(150)
data = np.zeros((150,4))
disto = []
for i in range(150):
    data[i][0] = q5a.data_lst[i][0]
    data[i][1] = q5a.data_lst[i][1]
    data[i][2] = q5a.data_lst[i][2]
    data[i][3] = q5a.data_lst[i][3]
    if i<50:
        desired[i] = 1
    elif i>=50 and i < 100:
        desired[i] = 2
    else:
        desired[i] = 3
lst = []
for i in range(150):
    lst.append(i)
np.random.shuffle(lst)
#first we compute the k means for the data_lst
#clusters = 10 # number of clusters
for clusters in range(1,21):
    print(clusters)
    means = np.random.rand(clusters,4) # initilisation of the means
    for i in range(clusters):
        means[i][0] = 6 + np.random.rand()
        means[i][1] = 2.5 +  np.random.rand()
        means[i][2] = 4.2 +  np.random.rand()
        means[i][3] = 1.5 +  np.random.rand()
    #print(means)
    #means = np.zeros((5,4))
    asgn = np.zeros(150)
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
            for j in range(150):
                if asgn[j] == i:
                     sum = sum + data[j]
                     count = count + 1
            if sum[0] + sum[1] + sum[2] + sum[3] != 0:
                means[i] = sum/count
    err = 0
    for i in range(clusters):
        set = 0
        versi = 0
        virg = 0
        count = 0
        for j in lst:
            if asgn[j] == i:
                count = count + 1
                if j<50:
                    set = set + 1
                elif j >=100:
                    virg = virg + 1
                else:
                    versi = versi + 1
        err = err + count - max(set,versi,virg)
    error.append(err*0.666)
    #print("Final")
    #print(means)

# now to plot
x_list = []
for i in range(1, 21):
       x_list.append(i)
plt.scatter(x_list,error)
plt.plot(x_list,error)
plt.xlabel("Clusters")
plt.ylabel("% Misclassication")
plt.title("Misclassification Graph")
plt.show()
'''
