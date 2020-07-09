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