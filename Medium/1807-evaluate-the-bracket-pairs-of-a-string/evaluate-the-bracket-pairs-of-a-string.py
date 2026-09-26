class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        output = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i = i+1 # for the ( bracket
                temp = []
                while s[i] != ')':
                    temp.append(s[i])
                    i = i + 1
                i = i + 1 # for the ) bracket
                output.append(d.get("".join(temp),"?"))
            else: # for non () characters
                output.append(s[i]) 
                i = i + 1
        return "".join(output)