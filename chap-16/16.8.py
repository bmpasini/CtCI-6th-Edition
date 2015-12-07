# Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").

def english_int(n):
    english = list()
    if n > 10 ** 9:
        billion = (n // (10 ** 9)) % 1000
        if billion != 0:
            english += convert(billion)
            english.append('billion,')
    if n > 10 ** 6:
        million = (n // (10 ** 6)) % 1000
        if million != 0:
            english += convert(million)
            english.append('million,')
    if n > 10 ** 3:
        thousand = (n // (10 ** 3)) % 1000
        if thousand != 0:
            english += convert(thousand)
            english.append('thousand,')
    if n > 0:
        hundred = n % 1000
        if hundred != 0:
            english += convert(hundred)
        return ' '.join(english)
    return 'zero'


def convert(n):
    units = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
    teens = [ 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]
    decimals = [ 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]
    english = list()
    hundred = n // 100
    decimal = n - hundred * 100
    unit = decimal % 10
    if decimal > 9 and decimal < 20:
        english.insert(0, teens[decimal % 10])
    else:
        if unit != 0 and decimal != 0:
            english.insert(0, units[unit])
        if decimal > 19:
            english.insert(0, decimals[decimal // 10 - 2])
    if hundred > 0:
        english.insert(0, 'hundred')
        english.insert(0, units[hundred])
    return english

    
if __name__ == "__main__":
    print(english_int(100))
    print(english_int(772))
    print(english_int(999))
    print(english_int(0))
    print(english_int(1))
    print(english_int(27))
    print(english_int(18))
    print(english_int(10))
    print(english_int(20))
    print(english_int(17772))
    print(english_int(177772))
    print(english_int(17177772))
    print(english_int(1717177772))
    print(english_int(19323984))