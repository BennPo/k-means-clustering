# need - X pos, y pos, what cluster, 
import numpy as np
from sklearn.datasets import make_blobs

import matplotlib.pyplot as plt

import random


class KMeansClustering():
    def __init__(self, X, y, k=3, width = 100, height = 100):
        self.X = X
        self.y = y
        self.k = k


    def init_centroids(self):
        self.centroids = np.array([[random.randint(0, 3), # x
                                    random.randint(0, 3) # y
        ] for _ in range(self.k)], dtype=float)
        

    def create_points(self):
        self.points = np.array(self.X)


    def find_distances(self):
        self.distances = np.sqrt(abs(np.sum((self.points[:, np.newaxis, :] - self.centroids[np.newaxis, :, :]) ** 2,  axis=2)))


    def get_idx(self):
        self.idx = np.argmin(self.distances, axis=1)
        self.idx = self.idx.reshape((100,1))


    def get_new_cluster(self):
        for a in range(self.k):
            if np.sum(np.where(self.idx == a, 1, 0)) != 0:
                self.new_centroid = np.array(np.sum(np.where(self.idx == a, self.points, 0), axis=0) / np.sum(np.where(self.idx == a, 1, 0)))
            else:
                self.new_centroid = self.centroids[a]

            self.centroids[a] = self.new_centroid
            print(np.shape(self.centroids))
      

        
    def display(self):
        for cluster in range(self.k):

            # Get all points that belong to this cluster
            cluster_points = self.points[self.idx.flatten() == cluster]

            # Plot the points
            plt.scatter(
                cluster_points[:, 0],
                cluster_points[:, 1],
                label=f"Cluster {cluster}"
            )

            # Plot the centroid
            plt.scatter(
                self.centroids[cluster, 0],
                self.centroids[cluster, 1],
                marker="X",
                s=200,
                edgecolors="black"
            )

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("K-Means Clustering")
        plt.legend()
        plt.show()


k = 4
X, y = make_blobs(n_samples=100, centers=k, n_features=2,
                  random_state=0)
test = KMeansClustering(X, y, k)
test.init_centroids()
test.create_points()
for _ in range(5):
    test.find_distances()
    test.get_idx()
    test.display()
    test.get_new_cluster()
test.display()

print(test.centroids)


