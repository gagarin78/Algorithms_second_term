import time
import sys

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        N = int(lines[0].strip())
        A1 = int(lines[1].strip())
        A2 = int(lines[2].strip())
        A3 = int(lines[3].strip())
        A4 = int(lines[4].strip())
        A5 = int(lines[5].strip())
        A6 = int(lines[6].strip())
        A7 = int(lines[7].strip())
    return N, A1, A2, A3, A4, A5, A6, A7

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

def minimal_printing_cost(N, A1, A2, A3, A4, A5, A6, A7):
    tariffs = [
        (1, A1),
        (10, A2),
        (100, A3),
        (1000, A4),
        (10000, A5),
        (100000, A6),
        (1000000, A7)
    ]
    
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        for count, cost in tariffs:
            if i >= count:
                dp[i] = min(dp[i], dp[i - count] + cost)
            else:
                dp[i] = min(dp[i], cost)
    
    return dp[N]

def main():
    start_time = time.time()
    
    input_filename = 'input.txt'
    N, A1, A2, A3, A4, A5, A6, A7 = read_numbers_from_file(input_filename)
    
    result = minimal_printing_cost(N, A1, A2, A3, A4, A5, A6, A7)
    
    output_filename = 'output.txt'
    write_result_to_file(output_filename, result)
    
    result_size = sys.getsizeof(result)
    execution_time = time.time() - start_time
    
    print(f"Минимальная стоимость: {result}")
    print(f"Общий размер памяти: {result_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    main()