import pickle
from patricia import trie
from recipe import *
from settings import *
import sys
PostingStruct = recordtype("PostingStruct", "df posting") # a struct consting of df and posting list
def main():
	for i in range(0,index_count):
		t = trie()
		with open(pickleFolder+'/'+sys.argv[1]+'/'+str(i)+'.pik', 'rb') as f:
				t = pickle.load(f)
		#a =  sorted(t.iter(''))
		for j in t:
			if j != "":
				print j , t[j]
if __name__ == '__main__':
  	main()
