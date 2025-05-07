from dag_toposort import matrix_topological_sort, list_to_matrix, topological_sort, generate_random_dag
import time
import csv
import os


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def run_benchmark(n):
    
    adj_list = generate_random_dag(n)
    matrix = list_to_matrix(adj_list)

    time_list = measure_time(topological_sort, adj_list)
    time_matrix = measure_time(matrix_topological_sort, matrix)
    return {
        "n" : n,
        "time_list" : round(time_list,6),
        "time_matrix" : round(time_matrix,6)
    }

def save_result_csv(data, filename, append=False):
    mode = 'a' if append else 'w'
    write_header = not append or not os.path.exists(filename)

    with open(filename, mode, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["n", "time_list", "time_matrix"])
        if write_header:
            writer.writeheader()
        writer.writerow(data)
            