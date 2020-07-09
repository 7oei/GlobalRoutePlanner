#!/usr/bin/env python3

import numpy as np
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def get_euclidean_distance(cities, N, dist):

    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    return dist

# It takes into account the distribution of the cost of edges leaving a node.
# If the distance average of both end nodes is large, we need to choose the edges 
# with priority for preventing from getting local opitimal solution.
def minus_mean_distance(dist, N):

    ave_dist = np.mean(dist, axis=1)
    dist = [[dist[i][j] - (ave_dist[i] + ave_dist[j])
            for i in range(N)] for j in range(N)]
    return dist


def minus_k_mean_distance(dist, N, k):

    ave_dist = np.mean(np.sort(dist, axis=1)[:, 1:min(N, k + 1)], axis=1)
    dist = [[dist[i][j] - (ave_dist[i] + ave_dist[j])
            for i in range(N)] for j in range(N)]
    return dist