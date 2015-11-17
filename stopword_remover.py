from __future__ import print_function
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
import sys, os

#stop_words_from_nltk = set(stopwords.words('english'))

#print(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'stopwords.txt'))

with open('punc_and_ocr.txt', 'r') as stops:
    s = stops.read()
    stop_words_from_file = s.split()

stop_words_from_file = set(stop_words_from_file)

#total_stop_words_set = stop_words_from_file.union(stop_words_from_nltk)
total_stop_words_set = stop_words_from_file

def is_utf8(s):
	try:
		s.decode('utf-8')
		return True
	except UnicodeError:
		return False

def is_ascii(s):
	return all(ord(c) < 128 for c in s)

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass
	return False

def stopword_remover(input, output):
	with open(input,'r') as inFile, open(output,'w') as outFile:
		for line in inFile:
			words = line.split()
			tokens = [w for w in words if not (w in total_stop_words_set or is_number(w) or ((not is_ascii(w)) and len(w) < 4))]
			if len(tokens) > 3:
				print(' '.join([t for t in tokens]), file=outFile)


if __name__ == "__main__":
	inFile = sys.argv[1]
	outFile = sys.argv[2]
	stopword_remover(inFile, outFile)