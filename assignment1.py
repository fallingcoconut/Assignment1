__author__ = 'kelvinwu'
from nltk.book import *
from matplotlib import pylab

def first_and_last(text1, M):
    print(text1[-M:])
    print(text1[:M])


def percentage(count, total):
    return round(count / total * 100, 2)


def word_percentage(text, string):
    searchcount = text.count(string)
    totalcount = len(text)
    return searchcount, percentage(searchcount, totalcount)


def unique_words(text):
    uniquewords = len(set(text))
    lowercasewords = len(set(w for w in text if w.islower()))
    uppercasewords = len(set(w for w in text if w.isupper()))
    alllowerwords = len(set(w.lower() for w in text))
    return uniquewords, lowercasewords, uppercasewords, alllowerwords


def words_cumulative(text, K):
    fdist = FreqDist(text)
    most_common = fdist.most_common(K)
    key = list(w[0] for w in most_common)

    percentages = list(word_percentage(text, w)[1] for w in key)

    print(list(percentages))
    pylab.xticks(range(len(key)), key)
    pylab.ylim(0, 100)
    pylab.plot(range(len(key)), percentages)


first_and_last(text3, 10)
first_and_last(text4, 10)
first_and_last(text6, 10)

print(word_percentage(text1, 'the'))
words_cumulative(text1, 50)
words_cumulative(text3, 50)
words_cumulative(text5, 50)