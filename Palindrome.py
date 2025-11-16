def isPalindrome(self, s: str) -> bool:
    import re

    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = s.lower()

    if s[::-1] == s:
        return True
    else:
        return False
