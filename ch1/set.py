from n_gram import n_gram

word1 = "paraparaparadise"
word2 = "paragraph"

bi_grams_w1 = n_gram(word1, 2, "char")
tuples_w1 = [tuple(x) for x in bi_grams_w1]

bi_grams_w2 = n_gram(word2, 2, "char")
tuples_w2 = [tuple(x) for x in bi_grams_w2]

if __name__ == "__main__":
    print("union: ", set(tuples_w1) | set(tuples_w2))
    print("intersection: ", set(tuples_w1) & set(tuples_w2))
    print("difference: ", set(tuples_w1) - set(tuples_w2))

    print("bigram 'se' in w1: ", ("s", "e") in tuples_w1)
    print("bigram 'se' in w2: ", ("s", "e") in tuples_w2)
