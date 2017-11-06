import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# raw data and initialization
w1 = [[0,0,0],[1,0,0],[1,0,1],[1,1,0]]
w2 = [[0,0,1],[0,1,1],[0,1,0],[1,1,1]]
W0 = np.array([-1,-2,-2,0])

datas = w1 
datas.extend(w2)
X = []; Y = []; Z = []
for i in range(0,len(datas)):
    if i<4:
        datas[i].append(1)
    else:
        datas[i].append(-1)
    X.append(datas[i][0])
    Y.append(datas[i][1])
    Z.append(datas[i][2])

datas = np.array(datas)


# plot two type of the data with two colors
fig = plt.figure()
ax = plt.subplot(111,projection='3d')
ax.scatter(X[:4], Y[:4], Z[:4], c='r')
ax.scatter(X[4:], Y[4:], Z[4:], c='m')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')

def sign(W, coordinate):
    if (sum(W[0:3]*coordinate) + W[3]) > 0:
        return 1
    else:
        return -1

def perception(datas, W0, iteration, eta):
    W = W0
    itera = 0
    while True:
        if itera > iteration:
            break
        num = 0
        for data in datas:
            itera += 1
            out_put = sign(W, data[0:3])
            if data[3] != out_put:
                detlaW = np.dot((data[3]-out_put), data[:4])
                W = W + np.dot(eta, detlaW)
                num += 1
        if num == 0:
            break
        else:
            print(num)
    return W

# plot the division surface
W = perception(datas, W0, 30*8, 0.01)
print(W)
X=[]; Y=[]; Z=[]
X = np.arange(-0.2,1.2, 0.05)
Y = np.arange(-0.2,1.2, 0.05)
X, Y = np.meshgrid(X, Y)
Z = - (W[0]/W[2])*X - (W[1]/W[2])*Y - W[3]/W[2]
surf = ax.plot_surface(X, Y, Z)
plt.title("perception algorithm result")
plt.show()
