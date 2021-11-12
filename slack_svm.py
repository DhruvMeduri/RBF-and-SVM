# We SVM with slack variables- Versicolor and Virginica
import q5b
import numpy as np
from numpy import array, dot
from qpsolvers import quadprog_solve_qp
import random
desired = np.zeros(100)
data = np.zeros((100,75))
err = []
for i in range(50,150):
    data[i-50][0] = q5b.data_lst[i][0]
    data[i-50][1] = q5b.data_lst[i][1]
    data[i-50][2] = q5b.data_lst[i][2]
    data[i-50][3] = q5b.data_lst[i][3]
    data[i-50][4] = q5b.data_lst[i][4]
    if i<100:
        desired[i-50] = 1
    else:
        desired[i-50] = -1
lst = []
err = 0
for i in range(100):
    lst.append(i)
training = []
testing = []
np.random.shuffle(lst)
for i in range(70):
    training.append(lst[i])
for i in range(70,100):
    testing.append(lst[i])

data = np.array(data)
#Now we define the matrices required in the qp
P = np.zeros((75,75))
for i in range(75):
    for j in range(75):
        if i == j and i ==0:
            P[i][j] = 10**(-10)
        if i == j and i>=5:
            P[i][j] = 10**(-10)
        if i == j and i<5 and i!=0:
            P[i][j] = 1
G = np.zeros((70,75))
h = np.zeros(70)
q = np.zeros(75)
for i in range(75):
    if i>=5:
        q[i] = 1000000#User Defined Constant
A = np.zeros((70,75))
b = np.zeros(70)
lb = 0
ub = np.Inf
for i in range(70):
    for j in range(5):
        G[i][j] = -data[training[i]][j]*desired[training[i]]
    G[i][i+5] = 1/desired[training[i]]
for i in range(70):
    h[i] = -1

weights = quadprog_solve_qp(P, q, G, h, A , b, lb, ub)
#print("QP solution: ",weights[0],weights[1],weights[2],weights[3],weights[4])


#for computing Error
for i in testing:
    predict = np.dot(weights,data[i])
    if desired[i] == 1 and predict<-1:
        err = err + 1
    elif desired[i] == -1 and predict>1:
        err = err + 1

#print("% Error: ",err*3.333)
