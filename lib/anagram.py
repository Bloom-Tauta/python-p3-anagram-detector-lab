# your code goes here!

class Anagram:
    def __init__(self, word):
        self._word = word

    def match(self, word_list):
        list = []
        for candidate in word_list:
            if self.is_anagram(candidate):
                list.append(candidate)
        
        return list
    
    def is_anagram(self, candidate):
        cleaned_words = self._word.lower().replace(' ', '')
        cleaned_candidate = candidate.lower().replace(' ', '')
        return sorted(cleaned_words) == sorted(cleaned_candidate)
        

'''
we need to iterate over the list.
check if the letter is equal to letter in the list
return true and set it to self.letter
return empty list if the words do not match
'''