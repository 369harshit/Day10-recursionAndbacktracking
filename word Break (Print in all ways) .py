class WordBreak:
    
    def wordBreak(self, s, wordDict):
        
        # function that will perform word break
        # and return True or False
        def wordBreakRecursion(str, wordDict, start):
        
            # base case to check whether
            # the whole string is exhausted,
            # in that case return a `true`
            if start == len(s):
                return True
            
            # check every possible prefix
            # of the string in the 
            # dictionary of words.
            for end in range(start + 1, len(s) + 1):
                
            # If substring is found in the `worddict`, 
           # recursively call the function
           # for the remaining portion
           # of the string.
                if s[start:end] in wordDict and wordBreakRecursion(s, wordDict, end):
                    return True
            
        # If the substring is not found and
        # all the substrings has being checked
        # return a `False`
            return False

        return wordBreakRecursion(s, set(wordDict), 0)

#driver code

# creating object of WordBreak() class
ob = WordBreak()
# calling our wordBreak function
ans = ob.wordBreak("leetcode",["leet","code"])
# displaying results
print(ans)