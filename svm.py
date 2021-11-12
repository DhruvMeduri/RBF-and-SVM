# first we implement classification of setosa and versicolor
import q5b
import numpy as np
from numpy import array, dot
from qpsolvers import quadprog_solve_qp
import random
import matplotlib.pyplot as plt
'''
# We implement classification of setosa and versicolor
desired = np.zeros(100)
data = np.zeros((100,5))
err = []
for i in range(100):
    data[i][0] = q5b.data_lst[i][0]
    data[i][1] = q5b.data_lst[i][1]
    data[i][2] = q5b.data_lst[i][2]
    data[i][3] = q5b.data_lst[i][3]
    data[i][4] = q5b.data_lst[i][4]
    if i<50:
        desired[i] = 1
    else:
        desired[i] = -1
lst = []
err = 0
for i in range(100):
    lst.append(i)
np.random.shuffle(lst)
training = []
testing = []
for i in range(70):
    training.append(lst[i])
for i in range(70,100):
    testing.append(lst[i])
data = np.array(data)
#Now we define the matrices required in the qp
P = np.array([[10**(-10),0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],dtype='float')
G = np.zeros((70,5))
h = np.zeros(70)
q = np.zeros(5)
A = np.zeros((5,5))
b = np.zeros(5)
for i in range(70):
    for j in range(5):
        G[i][j] = -data[training[i]][j]*desired[training[i]]
for i in range(70):
    h[i] = -1

weights = quadprog_solve_qp(P, q, G, h, A, b)
print("QP solution: x = {}".format(weights))

#for computing Error

for i in testing:
    predict = np.dot(weights,data[i])
    if desired[i] == 1 and predict<-1:
        err = err + 1
    elif desired[i] == -1 and predict>1:
        err = err + 1

print("% Error: ",err)

#plotting decision boundaries-(Not asked in the question)
for i in lst:
    plt.scatter(data[i][2],data[i][3],color = 'blue')

x = np.linspace(-1,4,100)
y = (-weights[2]/weights[3])*x + (-weights[0]/weights[3])
plt.plot(x,y,color='blue')
plt.show()
'''
# We implement classification of setosa and Virginica
desired = np.zeros(100)
data = np.zeros((100,5))
err = []
for i in range(50):
    data[i][0] = q5b.data_lst[i][0]
    data[i][1] = q5b.data_lst[i][1]
    data[i][2] = q5b.data_lst[i][2]
    data[i][3] = q5b.data_lst[i][3]
    data[i][4] = q5b.data_lst[i][4]
    desired[i] = 1
for i in range(100,150):
    data[i-50][0] = q5b.data_lst[i][0]
    data[i-50][1] = q5b.data_lst[i][1]
    data[i-50][2] = q5b.data_lst[i][2]
    data[i-50][3] = q5b.data_lst[i][3]
    data[i-50][4] = q5b.data_lst[i][4]
    desired[i-50] = -1
lst = []
err = 0
for i in range(100):
    lst.append(i)
np.random.shuffle(lst)
training = []
testing = []
for i in range(70):
    training.append(lst[i])
for i in range(70,100):
    testing.append(lst[i])
data = np.array(data)
#Now we define the matrices required in the qp
P = np.array([[10**(-10),0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],dtype='float')
G = np.zeros((70,5))
h = np.zeros(70)
q = np.zeros(5)
A = np.zeros((5,5))
b = np.zeros(5)
for i in range(70):
    for j in range(5):
        G[i][j] = -data[training[i]][j]*desired[training[i]]
for i in range(70):
    h[i] = -1

weights = quadprog_solve_qp(P, q, G, h, A, b)
print("QP solution: x = {}".format(weights))

#for computing Error

for i in testing:
    predict = np.dot(weights,data[i])
    if desired[i] == 1 and predict<-1:
        err = err + 1
    elif desired[i] == -1 and predict>1:
        err = err + 1

#print("% Error: ",err*3.333)
'''
#plotting decision boundaries-(Not asked in the question)
for i in lst:
    plt.scatter(data[i][1],data[i][3],color = 'blue')

x = np.linspace(-1,10,100)
y = (-weights[1]/weights[3])*x + (-weights[0]/weights[3])
plt.plot(x,y,color='blue')
plt.show()
'''
