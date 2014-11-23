Project Guide : 	
Dr. S. Ranbir Singh<br> 
Associate Professor, Indian Institute of technology, Guwahati

<h3>What is an Information Retrieval System?</h3>
Simply put, an IR system allows it users to efficiently search documents and retrieve meaningful information based on a search text/query. <br><br>
![alt tag](https://raw.github.com/sudhanshumittal/Information-retrieval-system/master/images/img.gif)
<br>
A good IR system should -<br>
a) be fast<br>
b) be space efficient<br>
c) be accurate<br>
d) understand the users query in an 'intelligent' manner<br><br>

<h3>What constitutes this project?</h3><br>
This project is a simple IR system with the following constituents -<br>
1) an efficient document indexing data structure<br>
2) a ranking algorithm to retrieve the most relevant documents to a query<br>
3) a page ranking algorithm to order the retrieved documents based on their 'importance'<br>
4) a summarization algorithm to display the summary of each document with its web link<br>


<h3>How to use it?  </h3>
	goto src directory
	run python main.py [-c] ( -c for index rebuilding )

<i>Note: This system can be integrated with a web based UI by calling the appropriate API from the package. However, The UI developed for the project has not been added to Github.</i><br>

<h3>Details for nerds</h3>
<table>
stopwords - using the list of stop words provided for the corpus<br>
stemming - using porter stemming implemented in python<br>
indexing - trie using bio library in python<br>
ranking  - Tf-IDf,  tf => augmented <br>
precision -	mean average precision ~ 1.4<br>
page ranking -google page ranks calculated in matlab<br>
summarization- supervised keyphrase extraction<br>
</table>

