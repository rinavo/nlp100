def cipher(text):
    return ''.join([chr(219 - ord(c)) if c == 'c' else c for c in text])

if __name__ == '__main__':
    print(cipher('Rin is a cat.'))