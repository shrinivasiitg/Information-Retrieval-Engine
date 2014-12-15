import pickle
    
def create_stopword_list(stopword_file):
	stopwords = []
	for word in open(stopword_file):
		stopwords.append(word.strip())

	"""with open('stopWords.pik', 'wb') as f:
		pickle.dump(stopwords, f, -1)
	"""
	return stopwords	
def remove_stopwords(wordList, stopwords):

    assert isinstance(wordList, list)
    assert isinstance(stopwords, list)

    return [x for x in wordList if x not in stopwords]

def tokenize(data):

    assert isinstance(data, basestring)
    return re.findall('\w+', data.lower())


