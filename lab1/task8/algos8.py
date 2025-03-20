import time
import sys

def max_lectures(lectures):
    lectures.sort(key=lambda x: x[1])  
    count = 0
    last_end = 0
    for s, f in lectures:
        if s >= last_end:
            count += 1
            last_end = f
    return count

def read_lectures_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        N = int(lines[0].strip())  
        lectures = []
        for i in range(1, N + 1):
            s, f = map(int, lines[i].strip().split())
            lectures.append((s, f))
    return lectures

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

def main():
    start_time = time.time()
    
    input_filename = 'input.txt'
    lectures = read_lectures_from_file(input_filename)
    
    result = max_lectures(lectures)
    
    output_filename = 'output.txt'
    write_result_to_file(output_filename, result)
    
    result_size = sys.getsizeof(result)
    execution_time = time.time() - start_time
    print(f"Максимальное количество лекций: {result}")
    print(f"Общий размер памяти: {result_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    main()