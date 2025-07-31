class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output=""
        actual_output=0
        for i in range(len(s)):
            if s[i] in output:
                index=output.index(s[i])
                output=output[index+1:]
            output+=s[i]
            if len(output)>actual_output:
                actual_output=len(output)
        return actual_output
                
        