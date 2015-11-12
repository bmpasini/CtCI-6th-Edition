class TrieNode(object):

    def __init__(self, character=None, terminates=False):
        self.character = character
        self.terminates = terminates
        self.children = dict()

    def add_child(self, character):
        self.children[character] = TrieNode(character)

    def get_child(self, character):
        try:
            return self.children[character]
        except KeyError:
            return None

    def get_terminates(self):
        return self.terminates

    def set_terminates(self, flag):
        self.terminates = flag

    def getChar(self):
        return self.character

    def add_word(self, word):
        if word is None or len(word) == 0:
            return None
        x = self
        for c in word:
            if x.get_child(c) is None:
                x.add_child(c)
            x = x.get_child(c)
        x.set_terminates(True)

    def add_words(self, list_of_words):
        for s in list_of_words:
            self.add_word(s)


class Trie(object):

    def __init__(self, list_of_words=None):
        self.root = TrieNode()
        self.root.add_words(list_of_words)

    def add_word(self, word):
        self.root.add_word(word)

    def add_words(self, list_of_words):
        self.root.add_word(list_of_words)

    def contains(self, word, exact=False):
        x = self.root
        for c in word:
            x = x.get_child(c)
            if x is None:
                return False
        return not exact or x.get_terminates()

    def get_root(self):
        return self.root


if __name__ == "__main__":
    words = [ "welcome", "to", "jamrock", "camp", "whe", "da", "thugs", "them", "camp", "at" ]
    t = Trie(words)
    print(t.contains("welc"))
    print(t.contains("jamrock", True))
    print(t.contains("camp"))
    print(t.contains("where"))
    print(t.contains("the"))
    print(t.contains("the", True))
    print(t.contains("them", True))
