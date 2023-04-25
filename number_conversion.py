number = int(input("Введите число: "))
base = int(input("Введите систему счисления числа (2-16): "))
convert_to_base = int(input("Введите систему счисления для конвертации (2-16): "))
if base < 2 or base > 16:
    print("Ошибка! Допустимые значения для системы счисления: от 2 до 16.")
else:
    if convert_to_base < 2 or convert_to_base > 16:
        print("Ошибка! Допустимые значения для системы счисления: от 2 до 16.")
    else:
        # перевод числа в десятичную систему
        decimal_number = 0
        digits = "0123456789ABCDEF"
        for i in range(len(str(number))):
            if str(number)[i].upper() not in digits[:base]:
                print("Ошибка ввода числа!")
                break
            decimal_number += digits.index(str(number)[i].upper()) * (base ** (len(str(number))-1-i))
        else:
            # перевод десятичного числа в заявленную систему счисления
            result = ""
            while decimal_number > 0:
                remainder = decimal_number % convert_to_base
                result += digits[remainder]
                decimal_number //= convert_to_base
            result = result[::-1]
            print("Результат конвертации:", result)
