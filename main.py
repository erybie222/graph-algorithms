from dag_toposort import matrix_topological_sort, list_to_matrix, topological_sort, generate_random_dag

if __name__ == "__main__":
    n = 6
    adj_list = generate_random_dag(n)
    print("Lista sąsiedztwa:", adj_list)

    order_list = topological_sort(adj_list)
    print("Sortowanie topologiczne (lista):", order_list)

    matrix = list_to_matrix(adj_list)
    order_matrix = matrix_topological_sort(matrix)
    print("Sortowanie topologiczne (macierz):", order_matrix)
