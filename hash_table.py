#Given a string s, find the length of the longest substring without duplicate characters.

s = "shalini"
print(len(s))

i = 0
j=0
substr = " "
while i < len(s)-1:
    if s[i] == s[i+1]:
        i = i+1
    else:
        sub = s[j:i+1:1]
        if len(sub) > len(substr):
            substr = sub
print(substr)