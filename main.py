import timeit
import random
import copy
import matplotlib.pyplot as plt

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def tim_sort(arr):
    return sorted(arr)

def main():
    num_elements = 10000
    num_trials = 10

    times_insertion = []
    times_merge = []
    times_tim = []
    
    for _ in range(num_trials):
        dataset = [random.randint(0, 10000) for _ in range(num_elements)]
        dataset_for_insertion = copy.deepcopy(dataset)
        dataset_for_merge = copy.deepcopy(dataset)
        dataset_for_tim = copy.deepcopy(dataset)

        t_insert = timeit.timeit(lambda: insertion_sort(dataset_for_insertion), globals=globals(), number=1)
        times_insertion.append(t_insert)

        t_merge = timeit.timeit(lambda: merge_sort(dataset_for_merge), globals=globals(), number=1)
        times_merge.append(t_merge)

        t_tim = timeit.timeit(lambda: tim_sort(dataset_for_tim), globals=globals(), number=1)
        times_tim.append(t_tim)

    average_time_insertion = sum(times_insertion) / num_trials
    average_time_merge = sum(times_merge) / num_trials
    average_time_tim = sum(times_tim) / num_trials
    
    print(f"Average time for insertion sort: {average_time_insertion} seconds")
    print(f"Average time for merge sort: {average_time_merge} seconds")
    print(f"Average time for Tim sort: {average_time_tim} seconds")

    plot_results(average_time_insertion, average_time_merge, average_time_tim)

def plot_results(average_time_insertion, average_time_merge, average_time_tim):
    # Names of algorithms
    algorithms = ['Insertion Sort', 'Merge Sort', 'Tim Sort']

    # Average times
    times = [average_time_insertion, average_time_merge, average_time_tim]

    # Creating the bar chart
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.bar(algorithms, times, color=['blue', 'green', 'red'])  # Create bars

    plt.yscale('log')

    # Adding titles and labels
    plt.title('Average Execution Time of Sorting Algorithms')
    plt.xlabel('Algorithms')
    plt.ylabel('Average Execution Time (seconds)')

    # Show the plot
    plt.show()
    

if __name__ == "__main__":
    main()
