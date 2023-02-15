def spell_out_number(num):
    if num == 0:
        return "zero"

    # dictionary for numbers and their spelled out versions
    num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
                90: 'ninety', 100: 'hundred', 1000: 'thousand'}

    if num in num_dict:
        return num_dict[num]

    if num < 100:
        tens = (num // 10) * 10
        ones = num % 10
        return f"{num_dict[tens]}-{num_dict[ones]}"

    if num < 1000:
        hundreds = num // 100
        tens = num % 100
        if tens == 0:
            return f"{num_dict[hundreds]} {num_dict[100]}"
        else:
            return f"{num_dict[hundreds]} {num_dict[100]} {spell_out_number(tens)}"

    if num < 10000:
        thousands = num // 1000
        hundreds = num % 1000
        if hundreds == 0:
            return f"{num_dict[thousands]} {num_dict[1000]}"
        else:
            return f"{spell_out_number(thousands)} {num_dict[1000]} {spell_out_number(hundreds)}"

    return "number out of range"


numb=int(input("Enter a number: "))
print(spell_out_number(numb))
