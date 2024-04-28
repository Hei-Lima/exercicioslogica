def conversor(number, base):
    result = ""
    base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"