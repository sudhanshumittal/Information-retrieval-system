import scipy.io
mat = scipy.io.loadmat('final.mat')

#print mat['final']
#print mat['final'][0]
#print mat['final'][0][9]

pagerank = {}
for x in range(0,len(mat['final'])):
   pagerank [ mat['final'][x][1] ] =   mat['final'][x][0]
   #print str(mat['final'][x][0]) + " "+str(mat['final'][x][1])
print pagerank[1]
#print str(len(mat['final']))