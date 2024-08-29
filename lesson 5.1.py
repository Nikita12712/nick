def calculate():
    try:
        expression = input("Введіть вираз для обчислення: ")
        result = eval(expression)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    while True:
        calculate()
        continue_calculation = input("Бажаєте продовжити? (y/yes для продовження): ").strip().lower()
        if continue_calculation not in ('y', 'yes'):
            print("Робота калькулятора завершена.")
            break

if __name__ == "__main__":
    main()
