import os
import nltk
from nltk.stem import *
from porter2 import stem
from nltk.stem.porter import *
import pickle
import xml.etree.ElementTree as ET
#import tfidf
from collections import defaultdict

#table = tfidf.tfidf()
# Giving Path of the files on the Desktop
path = "/home/lalit/Desktop/IR_LAB/Final_Index/Eng_code/eng/"

# declaring an array for all files to store

# declaring a dictionary for counting the words
freq = {}
inverted = {}
text = []
listOfWords = []
docs = []



stemmer = PorterStemmer()

# list oft he words which have to be removed for stemming

c = 0
# getting filename in the array files
for filename in os.listdir(path):
    #print(filename)
    c = c + 1
    print(c)

    filepath = path + filename

    # applying try and except to the "xml parsing"
    try:
        tree = ET.parse(filepath)
    except Exception as e:
        continue

    # tree = ET.parse(filepath, ET.XMLParser(encoding='utf-8'))

    # getting all the data in root variable which is parsed
    root = tree.getroot()
    text1 = ""
    text2 = ""
    text3 = ""

    if(root.findall('<DOCNO>') != -1):
        for k in root.findall('DOCNO'):
            text1 = k.text
            #print( text1)
        
    if(root.findall('<TITLE>') != -1):
        for k in root.findall('TITLE'):
            text2 = k.text

    if(root.findall('<TEXT>') != -1):
        for k in root.findall('TEXT'):
            text3 = k.text

    data =    text2 +  text3

    

    # removing punctuations from the data
    data = data.replace('\n', ' ')
    data = data.replace('|', ' ')
    data = data.replace('(', ' ')
    data = data.replace(')', ' ')
    data = data.replace('?', ' ')
    data = data.replace(',', ' ')
    data = data.replace(':', ' ')
    data = data.replace('!', ' ')
    data = data.replace('-', ' ')
    data = data.replace('.', ' ')
    data = data.replace("'", ' ')
    data = data.replace("  ", ' ')
    data = data.replace("/", ' ')
    data = data.replace("@", ' ')
    data = data.replace("%", ' ')
    data = data.replace("...", ' ')
    data = data.replace("=", ' ')
    data = data.replace('"', ' ')
    data = data.split()
    #print(len(data))
    stemwords = []
    fi = open('stop_eng.txt', 'r')
    stop = fi.read().split('\n')
    for word in data:
        if word not in stop:
            if not word.isdigit():
                stemwords.append(stemmer.stem(word))

#docs.append(listOfWords)
#print(file_dict)
    #listOfWords = [stemmer.stem(word) for word in data]

#print(len(listOfWords))
    single = list(stemwords)
#fo.write(str(listOfWords))    

    if True:
        for i in set(single):
                    if i in inverted.keys():  # checking for the word if it is in the inverted keys list
                        inverted[i].append((filename, single.count(i)))  
                    else:
                        inverted[i] = [(filename, single.count(i))]

#print(inverted)
fo = open('words.txt', 'w')
for j in inverted.keys():
#fo.write(str(set(listOfWords)))
    fo.write(str(j) + '\t\t')  # writing the word in the file
    fo.write(str(inverted.get(j)) + '\n')
    #print(str(i) + '\t\t' +str(inverted.get(i)) + '\n') 

# docs = [file_dict]
'''
collection = nltk.TextCollection(docs)
uniqTerms = list(set(collection))


#print(len(docs))

f = open('tf-idf.txt', 'w')
for doc in docs:
    #print(len(doc))
    for term in uniqTerms:

        f.write("%s \t\t\t : \t\t\t %f \n" % (term, collection.tf_idf(term, doc)))
'''        

    

    

 

