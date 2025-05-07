import random
from collections import deque

def topological_sort(adj_list):

    n = len(adj_list)
    indegree = [0] * n

    for u in range(n):
        for v in adj_list[u]:
            indegree[v] += 1

    queue= deque()        
    for u in range(n):
        if indegree[u] == 0:
                queue.append(u)

    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in adj_list[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return result
    
def list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0] * n for i in range(n)]
    for u in range(n):
        for v in adj_list[u]:
            matrix[u][v] = 1
    return matrix

def matrix_topological_sort(matrix):
    n = len(matrix)
    indegree = [0]  * n 

    for u in range(n):
        for v in range(n):
            if matrix[u][v] == 1:
                indegree[v] += 1

    queue = deque()

    for u in range(n):
        if indegree[u] == 0:
            queue.append(u)
    
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in range(n):
            if matrix[u][v] == 1:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
    return result

def generate_random_dag(n , density = 0.6):

    max_edges = n * ( n - 1 ) // 2
    num_edges = int(max_edges * density)   

    edges = []

    possible_edges = [(i,j) for i in range (n) for j in range(i + 1 , n)]
    random.shuffle(possible_edges)

    for u, v in possible_edges[:num_edges]:
        edges.append((u,v))

    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)

    return adj_list
