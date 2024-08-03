def rotate_pairs(words):
    def rotate(word):
        return [word[i:] + word[:i] for i in range(len(word))]
    word_set = set(words)
    pairs = set()
    for word in words:
        for rotated in rotate(word):
            if rotated in word_set and rotated != word:
                pairs.add(tuple(sorted((word, rotated))))
    return list(pairs)
wordlist = ["abc", "bca", "cab", "xyz", "yzx"]
print(rotate_pairs(wordlist))
