"""Write a class called Wordplay. It should have a field that holds a list of words. The user of the class should pass the list of words they want to use to the class. There should be the following methods:

• words_with_length(length) — returns a list of all the words of length length
• starts_with(s) — returns a list of all the words that start with s
• ends_with(s) — returns a list of all the words that end with s
• palindromes() — returns a list of all the palindromes in the list
• only(L) — returns a list of the words that contain only those letters in L
• avoids(L) — returns a list of the words that contain none of the letters in L"""

class Wordplay:
    def __init__(self, word_list):
        self.word_list = word_list
    def words_with_length(self, length):
        s = []
        for word in self.word_list:
            if len(word) == length:
                s.append(word)
        return s
    def starts_with(self, s):
        l = []
        for word in self.word_list:
            if word.startswith(s):
                l.append(word)
        return l
    def ends_with(self, s):
        pass
    def palindromes(self):
        pass
    def only(L):
        pass
    def avoids(L):
        pass
    
words = ["Come", "game", "market", "grace", "receive", "thanks", "people", "language"]
wordplay = Wordplay(words)
print(wordplay.words_with_length(6))
print(wordplay.starts_with("g"))