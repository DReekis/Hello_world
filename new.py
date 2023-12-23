
def int_to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""
    i = 0

    while num > 0:
        count = num // values[i]
        num %= values[i]

        while count > 0:
            roman += symbols[i]
            count -= 1

        i += 1

    return roman


