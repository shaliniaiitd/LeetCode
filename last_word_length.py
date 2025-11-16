#Given a string s consisting of words and spaces, return the length of the last word in the string.

def lengthOfLastWord(self, s: str) -> int:
    s = s.strip(' ')
    print(s)
    words = s.split(' ')
    print(words)
    return len(words[-1])