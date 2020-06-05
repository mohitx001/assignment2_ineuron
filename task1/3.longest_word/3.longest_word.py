"""
problem:
Implement a function longestWord() that takes a list of words and returns the longest one.
"""

def longestWord(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

a=input("enter the no. seperated by comma :")

b=a.split(',')
#print("list of enter word is:",b)
print("list of word is :",b,"\nlongest word from list is:",longestWord(b))