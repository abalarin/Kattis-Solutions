# About 9090 percent of the 300 billion emails sent every day are spam. Thus, a
# fast spam detection mechanism is crucial for large email providers. Lots of spammers
# try to circumvent spam detection by rewriting words like “M0n3y”, “Ca$h”, or “Lo||ery”.
#
# A very simple and fast spam detection mechanism is based on the ratios between
# whitespace characters, lowercase letters, uppercase letters, and symbols.
# Symbols are defined as characters that do not fall in one of the first three groups.
#
# The input consists of:
#
# --one line with a string consisting of at least 1 and at most 1000,000 characters.
# A preprocessing step has already transformed all whitespace characters to underscores (_),
# and the line will consist solely of characters with ASCII codes between 33 and 126 (inclusive).

def ratio(arg):
    return arg/total


spam_in = raw_input()

total = len(spam_in)
lowers = 0.0
uppers = 0.0
spaces = 0.0
specials = 0.0

for c in spam_in:
    if c.isupper():
        uppers+=1
    elif c.islower():
        lowers+=1
    elif c == '_':
        spaces+=1
    else:
        specials+=1
print(ratio(spaces))
print(ratio(lowers))
print(ratio(uppers))
print(ratio(specials))
