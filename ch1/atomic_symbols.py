first_letter_idx = {1, 5, 6, 7, 8, 9, 15, 16, 19}

sentence = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. '
            'New Nations Might Also Sign Peace Security Clause. '
            'Arthur King Can')

words = sentence.split()

res = {
    i: (w[0] if i + 1 in first_letter_idx else w[:2])
    for i, w in enumerate(words)
}

print(res)