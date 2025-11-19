import random


def gen(sentence):
    return [
        word[0] + shuffle(word[1:-1]) + word[-1] if len(word) > 4 else word
        for word in sentence.split()
    ]


def shuffle(word):
    chars = list(word)
    random.shuffle(chars)

    return "".join(chars)


if __name__ == "__main__":
    res = gen(
        "I couldn't believe "
        "that I could actually understand "
        "what I was reading : the phenomenal power of the human mind"
    )
    print(res)
