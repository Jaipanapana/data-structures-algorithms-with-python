class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def parenthesis(curr_str,open,close):
            if len(curr_str)==n*2:
                result.append(curr_str)
                return
            if open<n:
                parenthesis(curr_str+"(",open+1,close)
            if close<open:
                parenthesis(curr_str+")",open,close+1)
        parenthesis("",0,0)
        return result