def gronsfeld_code(message, key, op, alphabet):
    key *= len(message) // len(key) + 1
    message = message.lower()
    return ''.join([alphabet[alphabet.index(j) + int(key[i]) * op] for i, j in enumerate(message)])


def main():
    status = 0
    while status != 3:
        alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
        status = int(input('Press 1 for encrypt, 2 for decrypt and 3 to close the program \n'))
        if status == 1:
            message = input('Enter message for encryption \n')
            key = input('Enter key for ecnryption \n')
            print(gronsfeld_code(message, key, 1, alphabet))
        elif status == 2:
            message = input('Enter message for decryption \n')
            key = input('Enter key for decryption \n')
            print(gronsfeld_code(message, key, -1, alphabet))
        elif status != 3:
            print('Something wrong, try again')


if __name__ == "__main__":
    main()
