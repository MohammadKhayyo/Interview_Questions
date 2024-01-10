"""Design Add and Search Words Data Structure"""
"""Link to the problem: https://leetcode.com/problems/design-add-and-search-words-data-structure/"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


if __name__ == '__main__':
    trie = WordDictionary()
    trie.addWord("bad")
    trie.addWord("dad")
    trie.addWord("mad")
    Output = trie.search("pad")  # return False
    print(Output)
    Output = trie.search("bad")  # return True
    print(Output)
    Output = trie.search(".ad")  # return True
    print(Output)
    Output = trie.search("b..")  # return True
    print(Output)
