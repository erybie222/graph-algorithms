from dag_toposort import matrix_topological_sort, list_to_matrix, topological_sort, generate_random_dag
from benchmark import run_benchmark, save_result_csv, measure_time
from plots import plot_time_difference
import os
if __name__ == "__main__":
    n = 6
    elements = [500 , 1000, 1500, 2000, 2500, 3000, 3500 , 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]
    adj_list = generate_random_dag(n)
    print("Lista sąsiedztwa:", adj_list)

    order_list = topological_sort(adj_list)
    print("Sortowanie topologiczne (lista):", order_list)

    matrix = list_to_matrix(adj_list)
    order_matrix = matrix_topological_sort(matrix)
    print("Sortowanie topologiczne (macierz):", order_matrix)

    filename = 'wyniki.csv'

    if os.path.exists(filename):
        os.remove(filename)

    for n in elements: 
        result = run_benchmark(n)
        print(result)
        save_result_csv(result, filename, append=True)
    plot_time_difference(filename)
