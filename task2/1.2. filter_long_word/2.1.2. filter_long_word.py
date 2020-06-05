print()
print()
print('''
1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
''')

def filterlongword(string,number):
    return filter(lambda word:len(word)>number, string)

print(list(filterlongword(['Sunil', 'mohitj', 'Raju','Humanshu'], 4)))
print()
print()