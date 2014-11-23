import argparse, csv, re
#from corpus import *
#from numpy import *
from math import log
from stopWords import *
from create_corpus import *
from itertools import islice
import operator
import pickle
import sys

docCount  =0
maxFreq = {}
def rank( word, did, t):
	#augumented frequencies 
	global docCount
	#print 
	if docCount <= 0 :
		#print "docCOunt is zero"
		sys.exit()
	try:
		tf = 0.5 + (0.5* t[word][did]/maxFreq[did])
		idf = log( float(docCount)/(1+len(t[word])) )
		return tf*idf
	except Exception as inst:
		"""
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst  
		"""
		return 0
def take(n, iterable):
	return list(islice(iterable, n))
	#return 0
def create_data_str():
	print "finding stop words..."
	
	stop_words = create_stopword_list("../input/common_words")
	print "creating index..."
	user_input =  open("../input/cacm.all").read().lower().split()
	user_input = remove_stopwords(user_input, stop_words)
	corpus = create_corpus( user_input )
	print "storing queries..."
	readQuery()
	print "reading relevant documents"
	create_recall()
	#print "hello:"
def test(corpus, stop_words):
	recall = {}
	with open('qrels.pik', 'rb') as f:
		recall = pickle.load(f)
	q = open("../input/testQuery.txt").read().lower().split()
	q = remove_stopwords(q, stop_words)
	resultDocs = {}
	for word  in q:
		if not corpus.isPrefix(stem(word) ):	continue
		if not corpus[stem(word)]:	continue
		#print stem(word), corpus[stem(word)]
		
		try:
			for docID in corpus[stem(word)].items():
				#print docID
				r = rank(stem(word),docID[0], corpus)
		
				if not resultDocs.has_key(docID[0]):
					resultDocs[docID[0]] = r
				else:
					#if r > resultDocs[docID[0]]:
					resultDocs[docID[0]] += r
		except:
			pass
	#print resultDocs
	result =  take(10,sorted(resultDocs.iteritems(), key=operator.itemgetter(1), reverse=True))		
	#print result
	#print matches(recall['28'], result)
	#print precision(result, recall['28'])
	
	#print [x for x in recall['01'] if x,_ in result.]
def matches(a, b):
	count = 0
	for i,j in b:
		if i in a:
			count +=1
	return count
def main():
		if len(sys.argv) > 1:
			
			create_data_str()
		#return
		#import stop word list
		stop_words = create_stopword_list("../input/common_words")
		"""
		with open('stopWords.pik', 'rb') as f:
			stop_words = pickle.load(f)
		"""
		corpus = trie() 
		with open('trie.pik', 'rb') as f:
			corpus = pickle.load(f)	
		#user_input =  open("../input/cacm.all").read().lower().split()
		#user_input = remove_stopwords(user_input, stop_words)
		#print stop_words
		##verify that stop words have been removed
		#
		#create index
		#corpus = create_corpus( user_input )
		#for single query
		#return
		"""if any( k in stop_words for k in user_input ):
			print "true"
		else:
			print "false"
		"""
		
		global docCount
		global maxFreq
		with open('maxFreq.pik', 'rb') as f:
			docCount, maxFreq = pickle.load(f)
		#print "docCount is ", docCount
		
		#print corpus
		
		#print rank("tss", '1410', corpus )
		#test( corpus, stop_words)
		#return
		
		#import recall
		#readQuery()
		recall = {}
		with open('qrels.pik', 'rb') as f:
			recall = pickle.load(f)
		#import queries
		query = {}
		with open('query.pik', 'rb') as f:
			query  = pickle.load(f)
		tp = 0 
		
		#print rank ( 'articl', '1278', corpus)
		#print maxFreq['1278']
		#print 0.5 * (0.5* corpus['articl']['1278']/maxFreq['1278'])
		error = 0
	#	print corpus[' radio']
					
		for item in query.items():
			q = item[1]
			q = remove_stopwords(q, stop_words)
			#print item[0]
			#print q
			
			resultDocs = {}
			
			for word  in q:
				if not corpus.isPrefix (stem(word) ):
					#print "word not found ", word
					continue
				#if not corpus[stem(word)]:	continue
			
				try:
					for docID in corpus[stem(word)].items():
						#print docID
						#print docID
						
						
						r = rank(stem(word),docID[0], corpus)

						if not resultDocs.has_key(docID[0]):
							resultDocs[docID[0]] = r
						else:
							#if r > resultDocs[docID[0]]:
							resultDocs[docID[0]] += r
						
				except Exception as inst:
					"""print "corpus docID exception", word, docID
					print type(inst)     # the exception instance
					print inst.args      # arguments stored in .args
					print inst  
					"""
					pass
			result =  take(10,sorted(resultDocs.iteritems(), key=operator.itemgetter(1), reverse=True))		
			try:
				#print "AAA"
				item0 = int (item[0])
				if item0 not in recall.keys():	continue
				pres = precision( result, recall[item0])			
				#print "recall item[0] =", recall[item0]
				#print "result =", result
				#print "matches = ", matches(recall[item0], result)
				#print "pres =", pres
				tp += pres 
			except Exception as inst:
				"""
				print "pres Cal exception"
				print type(inst)     # the exception instance
				print inst.args      # arguments stored in .args
				print inst  
				"""
				pass
			#break
		#print "error =" , error
		print "mean average precision is ", tp/len(query)  
		#print resultDocs
		"""
		f= open("../stopWords.txt");	
		print '# documents =', len(corpus)
		print '# tokens =', sum(len(doc) for doc in corpus)
		print '# unique types =', len(corpus.alphabet)

		if args.output_file:
		    corpus.save(args.output_file)
		"""
if __name__ == '__main__':
  	main()
