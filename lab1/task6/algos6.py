import time
import sys

def largest_number(nums):
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x*10, reverse=True)
    largest_num = ''.join(nums)
    return largest_num if largest_num[0] != '0' else '0'

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
        numbers = list(map(int, data.split(',')))
    return numbers

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        file.write(result)

def main():
    start_time = time.time()
    input_filename = 'input.txt'
    numbers = read_numbers_from_file(input_filename)
    
    result = largest_number(numbers)
    
    output_filename = 'output.txt'
    write_result_to_file(output_filename, result)
    
    result_size = sys.getsizeof(result)
    execution_time = time.time() - start_time
    print(f"Наибольшее число: {result}")
    print(f"Общий размер памяти: {result_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    main()