def decimal_to_binary(decimal_number):
    binary = []
    while decimal_number >= 1:
        reszta = decimal_number % 2
        binary.append(reszta)
        decimal_number = decimal_number // 2

    binary.reverse()
    return binary
    
print("Wartość binarna liczby 14 to:")
print(decimal_to_binary(14))

def binary_to_decimal(binary_digits):
    # [0, 1 ,1 , 0]
    result = 0
    for i in range(len(binary_digits)):
        last_digit = binary_digits.pop()
        if last_digit == 1:
            result = result + pow(2, i)
    return result

print("Wartosć dziesietna liczby wynosi: ")
print(binary_to_decimal([1, 0, 1, 0, 0]))