def get_bigrams(text):
    bigrams_list = []
    n = len(text)

    for i in range(n - 1):
        bigram = text[i:i+1]
        bigrams_list.append(bigram)

    return bigrams_list