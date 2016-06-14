#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import random
import sys

class Markov(object):
	
	def __init__(self, file, size):
		self.size = int(size)
		self.words = self.get_words(file)
		self.word_chain = self.database()
		self.output = self.gen_text()

	def get_words(self, data):
		with open(data, 'rb') as f:
			return f.read().split()

	def database(self):
		word_dict = {}
		for x in range(len(self.words) - 2):
			word_dict.setdefault( (self.words[x], self.words[x+1]) , []).append(self.words[x + 2])	
		return word_dict

	def gen_text(self):
		starter = random.randint(0, len(self.words) - 2)
		w1, w2 = self.words[starter], self.words[starter+1]
		new_text = []
		for x in range(self.size-1):
			new_text.append(w1)
			## Debug - Shows choices for next word
			# print "Choices:", self.word_chain[(w1, w2)]
			w1, w2 = w2, random.choice( self.word_chain[(w1, w2)] )
		# Ending - Clean, find word with period, make first letter upper
		needs_period = True
		while needs_period:
			new_text.append(w1)
			try:
				w1, w2 = w2, random.choice( filter( lambda x: x[-1]== "." ,self.word_chain[(w1, w2)] ) )
				needs_period = False
			except IndexError:
				w1, w2 = w2, random.choice( self.word_chain[(w1, w2)] )
		new_text.append(w2)
		text = " ".join(new_text)
		text = text[0].upper() + text[1:]
		print text
		return text

if __name__ == "__main__":
	Markov(sys.argv[1], sys.argv[2])
