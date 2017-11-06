import matplotlib
import matplotlib.pyplot as plt 

data = [[0,0], [3,8], [2,2], [1,1], [5,3], [4,8], [6,3], [5,4], [6,4], [7,5]]

x = []; y = []
for d in data:
    x.append(d[0])
    y.append(d[1])
plt.figure(1)
plt.scatter(x,y)
plt.title('raw data')


import random
import numpy as np

def cal_distance(a,b):
    tmp = [a-b for a,b in zip(a,b)]
    return np.sqrt(sum(np.power(tmp,2)))

def cal_cost(center, cluster, data):
    cost = 0
    for c in cluster:
        cost += cal_distance(center, data[c])
    return cost

def cal_center(data, cluster):
    if len(cluster) == 0:
        raise "cluster has no data"
    center = np.zeros(len(data[0]))
    for c in cluster:
        center = [center+c for center,c in zip(center,data[c])]
    for i in range(len(center)):
        center[i] = center[i] / len(cluster)
    return center

def find_center(point, centers):
    dis_min = cal_distance(point, centers[0])
    center_index = 0
    for i in range(0,len(centers)):
        if dis_min > cal_distance(point, centers[i]):
            dis_min = cal_distance(point, centers[i])
            center_index = i
    return center_index

def k_means(data, k, max_iteration):
    """select k centers"""
    centers = []
    for i in range(0,k):
        centers.append(data[i])

    cost_trend = []
    cluster_result = []
    iternumber = 0
    while True:
        iternumber += 1
        """cluster"""
        clusters = []
        for i in range(0,k):
            clusters.append([]) 
        for i in range(0,len(data)):
            center_index = find_center(data[i], centers)
            clusters[center_index].append(i)
        """calculate the cost"""
        total_cost = 0
        for i in range(0,k):
            total_cost += cal_cost(centers[i], clusters[i], data)
        cost_trend.append(total_cost)
        print(total_cost)
        """判断一下是否有必要继续"""
        if iternumber == max_iteration:
            cluster_result = clusters
            break
        """update the center"""
        for i in range(0,k):
            center = cal_center(data, clusters[i])
            centers[i] = center
    return cost_trend, cluster_result

k = 3
iteration = 20
cost_trend, cluster_result = k_means(data, k, iteration)

"""plot cluster result"""
f2 = plt.figure(2)
color = ['m','c','r']
for i in range(0,k):
    for j in range(0,len(cluster_result[i])):
        index = cluster_result[i][j]
        cluster_result[i][j] = data[index]
        plt.scatter(data[index][0],data[index][1], color=color[i])
plt.title('cluster result')

"""plot loss trend"""
f3 = plt.figure(3)
plt.plot(cost_trend)
plt.title('loss trend')
plt.show()
