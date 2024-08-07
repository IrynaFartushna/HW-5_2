def calculator():
    while True:
        try:
            operation = input("Введіть обчислення (наприклад 10 - 4): ")
            result = eval(operation)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Помилка: {e}")

        continue_calculating = input(
            "Бажаєте продовжити роботу у калькуляторі? (введіть 'yes' для продовження, будь-яка інша клавіша для виходу): ").strip().lower()
        if continue_calculating not in ['yes']:
            print("Калькулятор закінчує свою роботу.")
            break

if __name__ == "__main__":
    calculator()
