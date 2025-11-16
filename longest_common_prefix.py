# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]
    print(type(prefix))

    for st in strs:
        print(st)
        while not st.startswith(prefix):
            prefix = prefix[:-1]
            print(prefix)

    return prefix