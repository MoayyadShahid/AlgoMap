# this implementation uses a list to store the child TrieNodes/pathways
class Trie:

    # we will store the child TrieNodes 
    # and whether this specific node in a sequence is a end of word character
    def __init__(self):
        # list of 26 children TrieNodes
        self.children = [None] * 26
        self.endChar = False
        
    # insert method
    def insert(self, word: str) -> None:
        # we need to traverse the Trie pathway so we first set out curr node 'self' to curr
        curr = self
        # we will loop through the trie by going through each character c
        for c in word:
            # we determine the position inside the children array of the characters of the word
            # by determining the index via arithmetic on ordinal values
            pos = ord(c) - ord('a')

            # we check if the character c exists or DOESN'T at the ordinal position in the children array
            if curr.children[pos] is None:
                # if it doesnt exist we create a TrieNode at the respective position
                curr.children[pos] = Trie()
            # then we update the curr node to iterate through the tree to the next node/character
            curr = curr.children[pos]

        # at the end of the word we set the final character as an end char True
        curr.endChar = True

    # in order to search we will basically do the same loop structure
    # but if we end up with a failure during accessing one of the children TrieNode's we return False
    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            pos = ord(c) - ord('a')

            if curr.children[pos] is None:
                return False
            curr = curr.children[pos]
        
        return curr.endChar
    
    # for startsWith we do the same thing as search but the only difference is that instead of checking if the
    # final character is an end char character we just return True as we are searching for a prefix
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            pos = ord(c) - ord('a')
            if curr.children[pos] is None:
                return False
            curr = curr.children[pos]
        
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)