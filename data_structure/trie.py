# coding=utf8
"""代码实现了最简单的字典树，只支持由小写字母组成的字符串。
在此代码基础上, 就可以实现比较复杂的字典树, 比如带统计数的, 或支持更多字符, 或支持删除等操作。
"""
class TrieNode(object):
    def __init__(self):
        # 是否构成一个完成的单词
        self.is_word = False
        self.children = [None] * 26


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        """Add a string to this trie."""
        p = self.root
        n = len(s)
        for i in range(n):
            loc = ord(s[i]) - ord('a')
            if p.children[loc] is None:
                new_node = TrieNode()
                if i == n - 1:
                    new_node.is_word = True
                p.children[loc] = new_node
                p = new_node
            else:
                p = p.children[loc]
                if i == n - 1:
                    p.is_word = True

    def search(self, s):
        """Judge whether s is in this trie."""
        p = self.root
        for c in s:
            p = p.children[ord(c) - ord('a')]
            if p is None:
                return False
        if p.is_word:
            return True
        else:
            return False


if __name__ == '__main__':
    trie = Trie()
    trie.add('str')
    trie.add('acb')
    trie.add('acblde')
    print(trie.search('acb'))
    print(trie.search('ac'))
    trie.add('ac')
    print(trie.search('ac'))
