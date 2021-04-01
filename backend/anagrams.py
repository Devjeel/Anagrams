
class Anagrams:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def check_anagram(self): 
        # the sorted strings are checked  
        if(sorted(self.s1) == sorted(self.s2)): 
            return (True, "{0} and {1} are anagrams!".format(self.s1, self.s2))
        else: 
            return (False, "{0} and {1} are not anagrams!".format(self.s1, self.s2))