if __name__ == '__main__':
    print('decimal to hexa-decimal converter using python')
    def decimal_to_hexadecimal():
        try:
            decimal_input = int(input('Enter a decimal number: - '))
            hex_out = hex(decimal_input)
            return hex_out
        except ValueError:
            raise ValueError('Invalid input. Please enter a valid decimal number.')
try:
    hexa=decimal_to_hexadecimal()
    print(hexa)
except ValueError as e:
    print(str(e))