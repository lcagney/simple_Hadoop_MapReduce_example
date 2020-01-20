#!/usr/bin/env python
import sys
from sklearn.feature_extraction import stop_words

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    #make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    stopwords = set(stop_words.ENGLISH_STOP_WORDS)
    punct = set([',','.',';',':','!','?','"','\''])
    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
		if word not in punct:
			 print '%s\t%s' % (word, "1")

