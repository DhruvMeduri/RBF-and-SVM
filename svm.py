# first we implement classification of setosa and versicolor
import q5b
import numpy as np
from numpy import array, dot
from qpsolvers import quadprog_solve_qp
import random
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
data = np.array(data)
#Now we define the matrices required in the qp
P = np.array([[10**(-10),0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],dtype='float')
#print(P.shape)
G = np.zeros((100,5))
#print(G.shape)
h = np.zeros(100)
#print(h.shape)
q = np.zeros(5)
#print(q.shape)
A = np.zeros((5,5))
b = np.zeros(5)
for i in lst:
    for j in range(5):
        G[i][j] = -data[i][j]*desired[i]
for i in range(100):
    h[i] = -1

weights = quadprog_solve_qp(P, q, G, h, A, b)
print("QP solution: x = {}".format(weights))

#for computing Error

for i in lst:
    predict = np.dot(weights,data[i])
    #print(desired[i])
    #print(predict)
    if desired[i] == 1 and predict<-1:
        err = err + 1
    elif desired[i] == -1 and predict>1:
        err = err + 1

print("% Error: ",err)
