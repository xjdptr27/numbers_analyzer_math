def count_and_sum_digits(n):
    """Количество и сумма цифр в числе"""
    num_str = str(n)
    count = len(num_str)
    total = sum(int(digit) for digit in num_str)
    return count, total

def reverse_number(n):
    """Поменять порядок цифр на обратный"""
    return int(str(n)[::-1])

def is_palindrome(n):
    """Проверить, является ли число палиндромом"""
    return str(n) == str(n)[::-1]

def find_palindromes_in_range(start, end):
    """Найти все палиндромы на отрезке"""
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes

def is_symmetric(n):
    """Проверить, является ли число симметричным"""
    num_str = str(n)
    length = len(num_str)
    if length % 2 != 0:
        return False
    half = length // 2
    return num_str[:half] == num_str[half:]

def digital_root(n):
    """Найти цифровой корень числа"""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Демонстрация работы всех функций
def main():
    # Пример использования
    number = 561
    
    print(f"Исходное число: {number}")
    print()
    
    # 1. Количество и сумма цифр
    count, total = count_and_sum_digits(number)
    print(f"1. Количество цифр: {count}, Сумма цифр: {total}")
    
    # 2. Обратное число
    reversed_num = reverse_number(number)
    print(f"2. Число в обратном порядке: {reversed_num}")
    
    # 3. Проверка на палиндром
    palindrome_check = "является" if is_palindrome(number) else "не является"
    print(f"3. Число {number} {palindrome_check} палиндромом")
    
    # 4. Поиск палиндромов на отрезке
    start, end = 100, 200
    palindromes = find_palindromes_in_range(start, end)
    print(f"4. Палиндромы на отрезке [{start}, {end}]: {palindromes}")
    
    # 5. Проверка на симметричность
    symmetric_check = "является" if is_symmetric(number) else "не является"
    print(f"5. Число {number} {symmetric_check} симметричным")
    
    # 6. Цифровой корень
    root = digital_root(number)
    print(f"6. Цифровой корень числа {number}: {root}")
    
    print("\n" + "="*50)
    
    # Дополнительные примеры
    print("\nДополнительные примеры:")
    
    # Пример с палиндромом
    palindrome_num = 1223221
    print(f"\nЧисло {palindrome_num}:")
    print(f"Паниндром: {is_palindrome(palindrome_num)}")
    print(f"Симметричное: {is_symmetric(palindrome_num)}")
    print(f"Цифровой корень: {digital_root(palindrome_num)}")
    
    # Пример с симметричным числом
    symmetric_num = 357357
    print(f"\nЧисло {symmetric_num}:")
    print(f"Паниндром: {is_palindrome(symmetric_num)}")
    print(f"Симметричное: {is_symmetric(symmetric_num)}")
    print(f"Цифровой корень: {digital_root(symmetric_num)}")

if __name__ == "__main__":
    main()
