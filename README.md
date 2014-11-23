Project Guide : 	
Dr. S. Ranbir Singh 
Associate Professor, Indian Institute of technology, Guwahati

What is an Information Retrieval System?
Simply put, an IR system allows it users to efficiently search documents and retrieve meaningful information based on a search text/query. 
![alt tag](https://raw.github.com/sudhanshumittal/Information-retrieval-system/master/images/img.gif)
A good IR system should -
a) be fast
b) be space efficient
c) be accurate
d) understand the users query in an 'intelligent' manner

What is this project about?
This project is a simple IR system with the following constituents -
1) an efficient document indexing data structure
2) a ranking algorithm to retirive the most relevant documents to a query
3) a page ranking algorithm to order the retieved documents based on their 'importance'
4) a summarization adorithm to display the summary of each document with its weblink


How do i use it?  
	goto src directory 
	run python main.py [-c]
	( -c controls index rebuilding )

Note: This system can be integrated with a webbased UI by calling the appropriate API from the package. However, The UI developed for the project has not been added to github.

Details for nerds -
stopwords
	using the list of stop words provided for the corpus
stemming 
	using porter stemming implememted in python
indexing 
	trie using bio library in python
ranking 
	tfidf
	tf => augumented 
precision
	mean average precision ~ 1.4
index size
	1.4 MB
page ranking
	google page ranks calculated in matlab
summarization
	supervised keyphrase extraction