import re,os
from bs4 import BeautifulSoup
from math import log
from os import walk
from nltk import PorterStemmer
from patricia import trie
from stopWords import *
from settings import *
import pickle
from recipe import *
import sys

PostingStruct = recordtype("PostingStruct", "df posting") # a struct consting of df and posting list
"""
#constants
#for bm25 scoring 
k1  = 1.6
b = 0.75
#TODO size[d], avdl, freq(qi, docID) 

def idf(docCount, df):
	return log( (docCount-df+0.5) / (df+0.5)  )
			  
def BM25(docID, query):
	ans = 0
	for qi in query.split(" "):
		ans += idf(qi) * ( freq(qi, docID)*(k1+1) ) /  ( freq(qi, docID) + k1*(1-b+b*size[d]/ avdl )
	return ans 
"""
def stem(a): #stems string a using porter Stemming
	
	a = PorterStemmer().stem_word(a)
	return a
	
def sec(word):
	if len(word) <2:
		return word[0]%index_count
	return (ord( word[0])*26+ord(word[1] )) % index_count
def createIndex(start):
	#create stop word file
	stopWords = create_stopword_list(stopwordsFile)
	counter=0
	#list of create patricia tries for various alphabets
	index = {}
	for i in range(0,index_count):
		index[i] = trie()
	
	#create index
	for folder in range(int(start), int(start)+1):
		print "working on folder"+ str(folder)
		#folder = os.walk(corpusFolder).next()[1]:
		for file in os.walk( corpusFolder+'/'+str(folder) ).next()[2]:
			try:
				#print file
				docID = file
				#ignore files other than the html files ( not of the form *.* )
				pattern = re.compile('\.')
				if pattern.search(file) != None:
					continue 
						
				#read html file
			
				html_doc = ""			
				try:
					html_doc =  open(corpusFolder+'/'+str(folder)+'/'+file).read() 
				except:
					print "could not open file "+file
					continue
				#create soup
				soup = BeautifulSoup(html_doc)
				#remove absurd tags like javascript, css, iframe
				[s.extract() for s in soup(['script', 'iframe', 'style'])]
				textList = []
				try:
					text = soup.get_text().encode("utf-8").lower()
					pattern =   re.compile("[^a-z0-9]")
					textList = re.split(pattern, text) 
				except Exception as e:
					print e 
					continue
			
				#remove stop words
				textList = remove_stopwords( textList, stopWords )
				#sort the text list to reduce the number of IOs
				textList = sorted(textList)
				#print textList
				#add words to appropriate patricia-trie
				for word in textList:
					#perform stemming
					word = stem(word)
					#remove small words
					if len(word) <= min_word_length:
						#print word#"word length insufficient"
						continue;
					#print word
					try:
						if not word in index[ sec(word) ] :	#the word has occured the first time
							index[sec(word)][word] = PostingStruct (0, {} ) #create posting list for the word
							#print index[sec(word)][word].df
				
						# the word has occured earlier	
						if index[ sec(word) ][word].posting.has_key(file) == True:
							index[ sec(word) ][word].posting[file] += 1
						else:
							index[ sec(word) ][word].posting[file] = 1
							index[ sec(word) ][word].df  += 1#index[ sec(word) ][word].df+1				
					except Exception as e:
						print word
						print e, word, sec(word)
						#return
				#break
				"""
				if counter == 3:
					break
				counter+=1
				"""
			except:
				continue
	#once all the tries have been created pickle them
	for i in range(0,index_count):
		with open(pickleFolder+'/'+start+'/'+str(i)+'.pik', 'wb') as f:
			pickle.dump(index[i], f, -1)
	print "successfully completed !"
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "invalid arguments"
	else:	 
		#for i in range(int(sys.argv[1]), int(sys.argv[1])+1):
		if not os.path.exists(pickleFolder+'/'+str(sys.argv[1])): os.makedirs(pickleFolder+'/'+str(sys.argv[1]))
	  	createIndex(sys.argv[1])
			
