number = int(input("Введите номер четверти системы координат: "))
quarters = "x > 0, y > 0", "x < 0, y > 0", "x < 0, y < 0", "x > 0, y < 0"
print(f"{number} -> {quarters[number-1]}")