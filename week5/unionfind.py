#!/usr/bin/env python3

class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def root(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.size[rx] += self.size[ry]
        self.parent[ry] = rx

    def issame(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

    def size(self, x):
        return self.size[self.root(x)]


if __name__ == '__main__':
    tree = UnionFind(5)
    tree.unite(0, 4)
    tree.unite(3, 4)
    for i in range(5):
        print(tree.root(i))