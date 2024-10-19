import heapq


def min_connection_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6, 7, 12, 1, 9]
print("Min cost:", min_connection_cost(cables))
