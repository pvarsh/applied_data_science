import re
first = """This is a very long string.  It has numbers like 15, 27, 34, 96 and letters like a,b,c r f and g.  Sometimes I forget to include commas but I always remember to do some things.  Because periods are important, especially this one.  And this one.  Too.  I know that this is kind of a boring sentence.  However, I really think it's great!  Data: 42,57,68,92,33"""

#finding all the numbers
result = re.search("[0-9]",first)
print result.start()
print first[49:64]
second = first[65:]
result = re.search("[0-9]",second)
print result.start()
print second[278:]

