import time
import sys

def can_eat_apples(n, s, apples):
    good_apples = []
    bad_apples = []
    
    for idx, (a, b) in enumerate(apples, 1):
        if b > a:
            good_apples.append((a, b, idx))
        else:
            bad_apples.append((a, b, idx))
    
    bad_apples.sort(key=lambda x: x[0] - x[1])
    
    for a, b, idx in good_apples:
        s -= a
        if s <= 0:
            return -1
        s += b
    
    for a, b, idx in bad_apples:
        s -= a
        if s <= 0:
            return -1
        s += b
    
    order = [idx for _, _, idx in good_apples + bad_apples]
    return order

def main():
    start_time = time.time()
    
    with open('input.txt', 'r') as file:
        n, s = map(int, file.readline().split())
        apples = []
        for _ in range(n):
            a, b = map(int, file.readline().split())
            apples.append((a, b))
    
    result = can_eat_apples(n, s, apples)
    
    with open('output.txt', 'w') as file:
        if result == -1:
            file.write("-1")
        else:
            file.write(" ".join(map(str, result)))
    
    result_size = sys.getsizeof(result)
    execution_time = time.time() - start_time
    
    print(f"Результат: {result}")
    print(f"Общий размер памяти: {result_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    main()