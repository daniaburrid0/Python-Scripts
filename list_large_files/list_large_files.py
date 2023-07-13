import os
import heapq
from pathlib import Path

def get_folder_path():
    folder_path = input("Please enter the folder path: ")
    while not os.path.isdir(folder_path):
        print("Invalid folder path. Please try again.")
        folder_path = input("Please enter the folder path: ")
    return folder_path

def get_n_largest_files():
    n = int(input("Please enter the number of largest files to display: "))
    while n <= 0:
        print("Invalid input. Please enter a positive integer.")
        n = int(input("Please enter the number of largest files to display: "))
    return n

folder_path = get_folder_path()
n_largest_files = get_n_largest_files()

def find_n_largest_files(folder_path, n):
    file_sizes = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            heapq.heappush(file_sizes, (-file_size, file_path))
            if len(file_sizes) > n:
                heapq.heappop(file_sizes)
                
    return [(-size, path) for size, path in file_sizes]

def print_files(files):
    for file_size, file_path in files:
        file_size_mb = file_size / (1024 * 1024)
        file_name = Path(file_path).name
        print(f"{file_name} - {file_size_mb:.2f} MB")

largest_files = find_n_largest_files(folder_path, n_largest_files)
print_files(largest_files)
