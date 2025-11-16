def convertToTitle(n: int) -> str:

    result = ''
    while n > 0:
        n, r = divmod(n - 1, 26)  # subtract 1 for 1-indexing, then divmod by 26
        result = chr(65 + r) + result  # prepend to result string instead of appending
    return result

title = convertToTitle(int(53))
print(title)