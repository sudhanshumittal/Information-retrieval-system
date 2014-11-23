from patricia import trie
from nltk import PorterStemmer
import pickle
import json
docCount = 0

def getFreq(l,id):
	#print l
	for t in l:
		if t[0] == id:
			return t[1]	
	return -1
def stem(a):
	a = a.strip('0123456789.,"[]()?!: ')
	a = PorterStemmer().stem_word(a)
	return a
def create_corpus( words ):
	maxFreq = {}
	unwanted = ['.b', '.x', '.n', '.c' ]
	wanted  = ['.i', '.t', '.a', '.w', '.k']
	i = 0
	t = trie()
	docID = 0
	global docCount 
	while i < len(words):
		freq = 1
		if words[i] == '.i':
			i=i+1
			docID = words[i]
			docCount +=1
			
		elif words[i] in unwanted: 
			i = 1+i
			while (words[i] not in wanted + unwanted) : 
				i = i+1
				
				if i >= len(words):
					break
#				print i, words[i], len(words)
			
		else:
			try:	
				#stem the word before insetion
				words[i] = stem(words[i]);
				#if new word 
				if t[ str(words[i]) ] == False:
					t[ str(words[i]) ] = {};
				if t[ str(words[i]) ].has_key(docID) == True:
					t[ str(words[i]) ][docID] += 1
				else:
					t[ str(words[i]) ][docID] = 1
				"""
				t[]
				f =  getFreq(t[str(words[i])],docID)
				#print str(words[i])
				#print f
				if f == -1:
					t[str(words[i])][docID] = freq#.append((docID,freq))
				else:
					#t[str(words[i])].remove((docID,f))
					if len(t[str(words[i])]) == 0:
						t[str(words[i])] = {}#[(docID,f+1)]
					else:
						t[str(words[i])][docID] = f+1#.append((docID,f+1))
				"""
			except KeyError:
				pass
				#no  key is present
				#print type(str(words[i]))
				#stem the word before insetion
				#words[i] = words[i].strip('0123456789., ')
				#words[i]  = PorterStemmer().stem_word(words[i])
				t[str(words[i])] = {}
				t[str(words[i])][docID] = 1
			contFreq = t[ str(words[i]) ][docID] 
			if maxFreq.has_key(docID):
				if maxFreq[docID] < contFreq:
					maxFreq[docID] = contFreq
			else:
				maxFreq[docID] = contFreq
			i= i + 1
	#print "docCount is ", docCount
	with open('maxFreq.pik', 'wb') as f:
		pickle.dump([docCount, maxFreq], f, -1)
	with open('trie.pik', 'wb') as f:
		pickle.dump( t, f, -1)
	#print t.keys()
	"""for word in t.keys():
			print word
			print t[word]
	"""
	#return t
def readQuery():
	#print "readQuery called"
	words =  open("../input/query.txt").read().lower().split()
	i = 0
	query = {}
	dels = ['.w','.i','.n'] 
	index = 1
		
	while i< len(words):
		if  words[i] == ".i" :
			i+=1
			index = words[i]
			#print index
		elif words[i] == ".w" :
			if not query.has_key(index):	query[index] = []
			i=i+1
			while (words[i] not in dels) and i<len(words) :
				query[index].append(stem(words[i]))
				i+=1
			
		else :
			i = i+1
			 
	with open('query.pik', 'wb') as f:
		pickle.dump(query, f, -1)
	#print query.keys()	
def create_recall( ):
	text  = open('../input/qrels.txt').read().split('\n')
	ans = {}
	i =0
	print len(text)
	while i < len(text)-1:
		line = text[i].split()
		#print text[i]
		if not ans.has_key(line[0]):	ans[ int(line[0]) ] =[]
		ans[ int (line[0]) ].append( line[1] )
		i +=1 
	with open('qrels.pik', 'wb') as f:
		pickle.dump(ans, f, -1)
	#print ans
def rel(relevant, i):
	if i in relevant:	return 1
	else:	return 0
def precision( result , relevant):
	sum  = 0.0
	relUpto = 0.0
	count = 0.0 
	for i in result: 
		count +=1.0
		r = rel(relevant, i[0])
		if r == 1:	relUpto +=1.0 
		sum += relUpto/count
		#print relUpto
	
	return sum/len(relevant)
