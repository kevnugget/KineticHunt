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


def get_neighbors(row, col, rows, cols):
    neighbors = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                neighbors.append((r, c))
    return neighbors


def find_words(board, trie):
    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(row, col, node, path, visited):
        letter = board[row][col]
        if letter not in node.children:
            return
        node = node.children[letter]
        path += letter
        if node.is_word:
            found.add(path)
        for r, c in get_neighbors(row, col, rows, cols):
            if (r, c) not in visited:
                visited.add((r, c))
                dfs(r, c, node, path, visited)
                visited.remove((r, c))

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, trie.root, "", {(row, col)})

    return found


def print_words_by_score(words):
    scores = {3: 100, 4: 400, 5: 800, 6: 1400, 7: 1800}

    def score(word):
        return scores.get(len(word), 2200 + 400 * (len(word) - 8))

    for word in sorted(words, key=lambda w: (-score(w), w)):
        print(f"{word} ({score(word)})")


def save_words_to_file(words, path):
    scores = {3: 100, 4: 400, 5: 800, 6: 1400, 7: 1800}

    def score(word):
        return scores.get(len(word), 2200 + 400 * (len(word) - 8))

    with open(path, "w", encoding="utf-8") as f:
        for word in sorted(words, key=lambda w: (-score(w), w)):
            f.write(f"{word} ({score(word)})\n")


def main():
    import sys

    if len(sys.argv) not in (3, 4):
        print("Usage: python word_hunt_solver.py <dictionary_path> <board_rows_comma_separated> [output_path]")
        print('Example: python word_hunt_solver.py words.txt "chas,reet,oldn,gima" results.txt')
        return

    dictionary_path, board_arg = sys.argv[1], sys.argv[2]
    board = [row.strip().lower() for row in board_arg.split(",")]

    trie = load_dictionary(dictionary_path)
    words = find_words(board, trie)
    print_words_by_score(words)

    if len(sys.argv) == 4:
        save_words_to_file(words, sys.argv[3])
        print(f"\nSaved results to {sys.argv[3]}")


if __name__ == "__main__":
    main()
