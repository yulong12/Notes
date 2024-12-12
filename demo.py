from concurrent.futures import ThreadPoolExecutor

def read_file(file_path):


    with open(file_path, 'r') as file:


        data = file.read()


        print(f"Read {len(data)} characters from {file_path}")


file_paths = ["file1.txt", "file2.txt", "file3.txt"]


with ThreadPoolExecutor(max_workers=5) as executor:  # 调整max_workers的值来优化性能


    executor.map(read_file, file_paths)

