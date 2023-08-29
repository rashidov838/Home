import re
"""
e - matches "e" symbol (if used with g flag would match any number of e's in string).
    e+ - match "e" at least once, where + means match preceding character at least once or infinite.
    ea? - match "e" and "a", but a is optional.
    ea* - match "e" and "a", but a is optional and can be infinite.
    . - match anything except newline.
    \symbol - ignores regex symbols, making them match what they actually is. Example: \. - matches .
    \w - match any word character
    \s - match any space character
    \S - match anything which is not whitespace
    \W - match anything which is not character
    \w{4} - match exactly 4 matches of regex
    {4,5} - 4 or 5 matches. {4,} - 4 or more matches
    [fc]at - grouping. matches "f" or "c" and "at": fat or cat
    | - same as "or" logic operator in programming
    (t|e|r){2,3}\. - matches "t or e or r" with length 2 to 3 character ending with period.
    ^ - beginning of the string
    $ - end of the string
    \d - matches any digits
    \d{3}[ -]?\d{3}[ -]?\d{4}
    (\d{3})[ -]?(\d{3})[ -]?(\d{4}) - grouping
    (?<areacode>\d{3})[ -]?(\d{3})[ -]?(\d{4})
    ((\+1)[ -]?)?\(?(?<areacode>\d{3})\)?[ -]?(\d{3})[ -]?(\d{4})"""


# regex.com - Для изучения 
pattern=re.compile("for")

full=re.compile("Look for the specific word for if you can ")
string="Look for the specific word for if you can "

print(re.search('specific',string))
# a=re.search('specific',string)
# print(a)
# print("group",a.group())
# print(a.span())
# print(a.start())
# print(a.end())

a=pattern.search(string)
print(a)

b=pattern.findall(string)
print(b)

c=full.fullmatch(string)
print(c)

pattern=re.compile(r"([a-zA-Z]).([p])")  # a-zA-Z любой символ должен заканчиваться с буквой p
string="123Look for pthe specific tword for you canp,:1 "
a=pattern.search(string)
print(a)
a=pattern.findall(string)
print(a)
a=pattern.finditer(string)
print(next(a))