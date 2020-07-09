#!/usr/bin/env python3

import sys
import math
import itertools
import numpy as np

from common import print_tour, read_input
from unionfind import UnionFind


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def two_opt(tour, dist):
    N = len(tour)

    while True:
        count = 0
        for i in range(N-2):
            for j in range(i+2, N):
                l1 = dist[tour[i]][tour[i + 1]]
                l2 = dist[tour[j]][tour[(j + 1) % N]]
                l3 = dist[tour[i]][tour[j]]
                l4 = dist[tour[i + 1]][tour[(j + 1) % N]]
                if l1 + l2 > l3 + l4:
                    new_tour = tour[i+1 : j+1]
                    tour[i+1 : j+1] = new_tour[::-1]
                    count += 1
        if count == 0:
            break
    return tour


def one_or_opt(tour, dist):
    N = len(tour)

    while True:
        count = 0
        for i in range(N):
            i0 = i
            i1 = (i + 1) % N
            i2 = (i + 2) % N
            for j in range(N):
                j0 = j
                j1 = (j + 1) % N
                if j0 not in {i0, i1}:
                    l1 = dist[tour[i0]][tour[i1]]
                    l2 = dist[tour[i1]][tour[i2]]
                    l3 = dist[tour[j0]][tour[j1]]
                    l4 = dist[tour[j0]][tour[i1]]
                    l5 = dist[tour[j1]][tour[i1]]
                    l6 = dist[tour[i0]][tour[i2]]
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        city = tour.pop(i1)
                        if i1 < j1:
                            tour.insert(j0, city)
                        else:
                            tour.insert(j1, city)
                        count += 1
        if count == 0:
            break
    return tour


def two_or_opt(tour, dist):
    N = len(tour)

    while True:
        count = 0
        for i in range(N):
            i0 = i
            i1 = (i + 1) % N
            i2 = (i + 2) % N
            i3 = (i + 3) % N
            for j in range(N):
                j0 = j
                j1 = (j + 1) % N
                if j0 not in {i0, i1, i2}:
                    l1 = dist[tour[i0]][tour[i1]]
                    l2 = dist[tour[i2]][tour[i3]]
                    l3 = dist[tour[j0]][tour[j1]]
                    l4 = dist[tour[j0]][tour[i1]]
                    l5 = dist[tour[j1]][tour[i2]]
                    l6 = dist[tour[i0]][tour[i3]]
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        if i2 == 0:
                            city1 = tour.pop(i1)
                            city2 = tour.pop(i2)
                            tour.insert(j0, city2)
                            tour.insert(j0, city1)
                        else:
                            city2 = tour.pop(i2)
                            city1 = tour.pop(i1)
                            if i1 < j1:
                                tour.insert(j0 - 1, city2)
                                tour.insert(j0 - 1, city1)
                            else:
                                tour.insert(j1, city2)
                                tour.insert(j1, city1)
                        count += 1
        if count == 0:
            break
    return tour
    

def get_euclidean_distance(cities, N, dist):

    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    return dist


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



def kruskal(dist, N, start):
    tree = UnionFind(N)
    relation = [[] for i in range(N)]
    one_array_dist = list(itertools.chain.from_iterable(dist))
    for k in np.argsort(one_array_dist):
        i = k % N
        j = int(k / N)
        if not tree.issame(i, j) and len(relation[i]) < 2\
           and len(relation[j]) < 2:
            relation[i].append(j)
            relation[j].append(i)
            tree.unite(i, j)
    
    def go_next():
        for i in range(len(relation[next_city])):
            if relation[next_city][i] in unvisited_cities:
                return relation[next_city][i]
        return None

    edge = []
    for i in range(N):
        if len(relation[i]) == 1:
            edge.append(i)
    relation[edge[0]].append(edge[1])
    relation[edge[1]].append(edge[0])

    current_city = start
    unvisited_cities = set(range(1, N))
    tour = [current_city]
    next_city = relation[current_city][0]
    while unvisited_cities:
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        next_city = go_next()

    return tour


# 総距離を計算
def total_distance(tour,dist):
    length = 0
    for i in range(len(tour)):
        length += dist[tour[i-1]][tour[i % len(tour)]]
    return length


def solve(cities):
    N = len(cities)
    sum_dis = 10**9

    dist = [[0] * N for i in range(N)]
    dist = get_euclidean_distance(cities,N,dist)
    
    for start in range (min(10, N)):
        tour = kruskal(dist, N, start)
        # tour = two_opt(tour, dist)
        # tour = one_or_opt(tour, dist)
        # tour = two_or_opt(tour, dist)

        # 最も距離の短いものを選択
        if sum_dis>total_distance(tour,dist):
            ans_tour = tour
            sum_dis = total_distance(tour,dist)

    return ans_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities=read_input(sys.argv[1])
    print_tour(solve(cities))