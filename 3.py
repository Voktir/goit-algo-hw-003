def hanoi(n, source, auxiliary, target, state):
    if n > 0:
        # Рекурсивно переміщуємо n-1 дисків з source на auxiliary
        hanoi(n - 1, source, target, auxiliary, state)
        
        # Переміщуємо найбільший диск з source на target
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        
        # Рекурсивно переміщуємо n-1 дисків з auxiliary на target
        hanoi(n - 1, auxiliary, source, target, state)

def solve_hanoi(n):
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'B', 'C', state)
    print(f"Кінцевий стан: {state}")

def main():
    while True:
        try:
            n = int(input("Введіть кількість дисків: "))
            if n <= 0:
                print("Кількість дисків має бути додатнім числом. Спробуйте ще раз.")
            else:
                break
        except ValueError:
            print("Будь ласка, введіть коректне число.")
    
    solve_hanoi(n)

if __name__ == "__main__":
    main()