import matplotlib.pyplot as plt
import csv


def plot_time_difference(filename):
    sizes = []
    list_times = []
    matrix_times = []


    with open(filename, 'r', newline='') as csvfile:    
        reader = csv.DictReader(csvfile)
        for row in reader:
            sizes.append(int(row['n']))
            list_times.append(float(row['time_list']))
            matrix_times.append(float(row['time_matrix']))


    plt.plot(sizes, list_times, label='Lista incydencji', color='blue', linewidth=2)
    plt.plot(sizes, matrix_times, label='Macierz sąsiedztwa', color='red', linewidth=2)


    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas operacji [s]')
    plt.title('Czas sortowania topologicznego w zależności od liczby wierzchołków')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()