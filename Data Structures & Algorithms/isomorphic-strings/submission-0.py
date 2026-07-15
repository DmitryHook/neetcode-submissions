class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        source_to_target = {}
        target_to_source = {}

        for s_char, t_char in zip(s, t):
            if s_char in source_to_target:
                if source_to_target[s_char] != t_char:
                    return False
            else:
                if t_char in target_to_source:
                    return False
                
                source_to_target[s_char] = t_char
                target_to_source[t_char] = s_char

        return True