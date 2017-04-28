import os
#import nltk
from porter2stemmer import Porter2Stemmer
#from nltk.stem import *
#from porter2 import stem
#from nltk.stem.porter import *
import pickle
import xml.etree.ElementTree as ET
#from nltk import word_tokenize

import string
#import tfidf
#from collections import defaultdict
#from PorterStemmer import PorterStemmer

class InvertedIndex():
    def __init__(self):
        
    
        path = "/home/lalit/Desktop/IR_LAB/Final_Index/EngFiles/Files/"                   #setting path of the
        indexing={}                                                                         
        f = open('result.txt','w')
        c = 0
        for inFile in os.listdir(path):                                                               #start of program       
            print(inFile)
            c = c + 1
            print(c)
            filepath = path + inFile
            try:
                tree = ET.parse(filepath)
            except Exception as e:
                continue
            
            root = tree.getroot()
            self.text1 = ""
            self.text2 = ""
            self.text3 = ""

            for k in root.findall('DOCNO'):
                    self.text1 = k.text
                    #print(self.text1)
                
            for k in root.findall('TITLE'):
                if(root.findall('<TITLE>') != -1):
                    self.text2 = k.text

            for k in root.findall('TEXT'):
                    self.text3 = k.text

            data =   self.text2 + self.text3
            
            punct = self.remove_punctuation(data)                                                  #removing punctuation
            final_text = self.stop_stem(punct)                                                       #removing stop wo
                                                                #stemming
            
            for j in set(final_text):                                                                    #indexing           
                if j in indexing.keys():
                    indexing[j].append((inFile, final_text.count(j)))
                else:
                    indexing[j]=[(inFile, final_text.count(j))]

        #for x in indexing.keys():
                #print(str(x) + '\t\t--->\t\t'  +  str(indexing.get(x)))
         #       f.write("%s  \t\t ---> \t\t  %s" %(x, indexing.get(x)) + '\n')


        pickle.dump(indexing, open("Inverted_Index.p", "wb"))



            
    def remove_punctuation(self, data):
        for punct in string.punctuation:
            data = data.replace(punct," ")

        data = data.replace('\t', ' ')
        data = data.split()
        #print(data)
        return data
                
    
    def stop_stem(self, data):
        stop=open("/home/lalit/Desktop/IR_LAB/Final_Index/Eng_code/stop_eng.txt").read().split("\n")
        stemwords = []
        stemmer = Porter2Stemmer()
        for word in data:
            if word not in stop:
                stemwords.append(stemmer.stem(word))    
        l = list(stemwords)
        return l


    
if __name__ == "__main__":
    obj = InvertedIndex()
