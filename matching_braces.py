


class Solution:
    def isValid(self, s: str) -> bool:
        expected = {")": "(", "}": "{", "]": "["}

        seen = []
        for el in s:

            if el not in expected.values() and el not in expected.keys():
                return False

            elif el in expected.keys() and expected[el] not in seen:
                return False


            elif el in expected.keys() and expected[el] == seen[-1]:
                seen.pop()
            else:
                seen.append(el)

        if len(seen) > 0:
            return False
        else:
            return True
