import timeit
import matplotlib.pyplot as plt
import platform


def insertion_sort(is_print_iteration, array):
    if is_print_iteration:
        print('Start: ' + str(array))

    for i in range(1, len(array)):
        key = array[i]

        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

        if is_print_iteration:
            print('Iteration ' + str(i) + ': ' + str(array))

    if not is_print_iteration:
        print('Final: ' + str(array))

def run_benchmark(input_size):
    setup_code = f"from __main__ import insertion_sort; import random; array = random.sample(range(1, {input_size + 1}), {input_size})"
    stmt = "insertion_sort(False, array.copy())"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=5)
    return execution_time


def create_plot(results):
    sizes, times = zip(*results)  # zip needed b/c of too many values to unpack warning
    plt.plot(sizes, times, marker='o', linestyle='-', color='b')
    plt.xlabel('Input Size of Array')
    plt.ylabel('Runtime (seconds)')
    plt.title('Insertion Sort Benchmark')
    plt.grid(True)
    plt.show()


def run_demo(arr):
    print('Demo testing Selection Sort:')
    insertion_sort(True, arr)


# runs test array and iterations to clearly see the sort
test_array = [4, 5, 2, 3, 1]
run_demo(test_array)

# runs the benchmark portion
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000]
time_results = []

for size in input_sizes:
    time = run_benchmark(size)
    time_results.append((size, time))
    print(f"Input Size: {size}, Execution Time: {time:.6f} seconds")

create_plot(time_results)