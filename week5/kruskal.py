#!/usr/bin/env python3

import sys
import math
import itertools
import numpy as np

from unionfind import UnionFind


def kruskal(dist, N):
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

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]
    next_city = relation[current_city][0]
    while unvisited_cities:
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        next_city = go_next()

    return tour