def is_year_leap(number):

    return "високосный" if number % 4 == 0 else "не високосный"


num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"Год {num} - {result}")
