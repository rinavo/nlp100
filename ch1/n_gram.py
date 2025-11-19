def n_gram(str, n, type):
    res = []
    if type == "word":
        words = str.split()
        for i in range(len(words) - n + 1):
            res.append(words[i : i + n])
    elif type == "char":
        for i in range(len(str) - n + 1):
            res.append(list(str[i : i + n]))
    return res

if __name__ == "__main__":
    input = "I am an NLPer"
    print(n_gram(input, 2, "word"))
    print(n_gram(input, 3, "word"))
    print(n_gram(input, 2, "char"))
    print(n_gram(input, 3, "char"))