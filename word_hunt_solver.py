class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children.setdefault(letter, TrieNode())
        node.is_word = True


def load_dictionary(path, min_length=3):
    trie = Trie()
    with open(path, encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if len(word) >= min_length and word.isalpha():
                trie.insert(word)
    return trie


def print_words_by_score(words):
    scores = {3: 100, 4: 400, 5: 800, 6: 1400, 7: 1800}

    def score(word):
        return scores.get(len(word), 2200 + 400 * (len(word) - 8))

    for word in sorted(words, key=lambda w: (-score(w), w)):
        print(f"{word} ({score(word)})")
