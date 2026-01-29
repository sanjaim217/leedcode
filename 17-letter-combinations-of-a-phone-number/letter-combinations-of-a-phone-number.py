class Solution:
    def add_char(self, current: str, digits: str): 
        # catcher
        if len(digits) == 0: 
            self.output_.append(current)
            return 
        
        for char in self.digit_characters[int(digits[0])]: 
            self.add_char(current + char, digits[1:])


    def letterCombinations(self, digits: str) -> List[str]:
        
        self.digit_characters = {2: "abc", 
                            3: "def", 
                            4: "ghi", 
                            5: "jkl", 
                            6: "mno", 
                            7: "pqrs", 
                            8: "tuv", 
                            9: "wxyz"}

        self.output_ = []
        self.add_char("", digits)
        
        return self.output_
        