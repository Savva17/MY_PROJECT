# Успешная посылка 116076847
def func_decrypting_string(string: str) -> str:
    """Функция для расшифровки сжатых команд и возвращает в строку."""
    result = []
    current_string = ''
    current_num = ''
    for char in string:
        if '0' <= char <= '9':
            current_num += char
        elif char == '[':
            result.append((current_string, int(current_num)))
            current_string = ''
            current_num = ''
        elif char == ']':
            last_string, num = result.pop()
            current_string = last_string + current_string * num
        else:
            current_string += char
    return current_string


if __name__ == '__main__':
    string = input()
    print(func_decrypting_string(string))
