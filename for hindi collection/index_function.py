import xml.etree.ElementTree as ET
import sys
import string
import os
#from PorterStemmer import PorterStemmer

class InvertedIndex():
    def __init__(self):
        self.exclude = list(string.punctuation)
        self.exclude.append('।')
        path = '/home/lalit/Desktop/IR_LAB/Final_Index/hindi/'                   #setting path of the file
        
        #all_files = glob.glob(files_path)                                                       #finds all the files which ends with extension .txt
        indexing={}                                                                        #creating a dictonary for indexing of files
        #documentid={}           #creating a dictonary for files storing file number of that particular file
        f = open('result.txt','w')
        c = 0
        for inFile in os.listdir(path):                                                               #start of program       
            print(inFile)
            c = c + 1
            print(c)
            filepath = path + inFile
            # applying try and except to the "xml parsing"
            try:
                tree = ET.parse(filepath)
            except Exception as e:
                continue
            # tree = ET.parse(filepath, ET.XMLParser(encoding='utf-8'))
            # getting all the data in root variable which is parsed
            root = tree.getroot()
            data = root[0].text + root[2].text
            #text = title + content                                                     #concatenating all the title and content in a single string text
            #print(text1)
            #f.write(text1)
                
            punct = self.punctuation(data)                                                  #removing punctuation
            stop = self.stop_words(punct)                                                       #removing stop words
            final_text= self.stemming(stop)                                                     #stemming
            if True:
                for j in final_text:                                                                    #indexing           
                    if j in indexing.keys():
                        indexing[j].append((inFile, final_text.count(j)))
                    else:
                        indexing[j]=[(inFile, final_text.count(j))]

        for x in indexing.keys():
                #print(str(x), '---', str(indexing.get(x)))
                f.write("%s  ----  %s" %(x, indexing.get(x)) + '\n')

            
    def punctuation(self, data):                                                            #Checking wether the word is punctuation or not if it is not punctuation concat with text or else leave it
        exclude = list(string.punctuation)
        exclude.append('।')
        exclude.append(',')
        exclude.append("''")
        exclude.append('""')
        exclude.append(':-')
        exclude.append(':')
        exclude.append('?')
        exclude.append(";")
        exclude.append('-')
        exclude.append('_')
        data = "".join(c for c in data if c not in exclude)
        return data
                
    
    def stop_words(self, data):                                                             #stop words file is linked in it and it searches if the text contains any stop words which are present in the file if yes then remove them
        stopWord=open("/home/lalit/Desktop/IR_LAB/Final_Index/stopwords.txt",encoding = 'utf-8').read().split("\n")
        text3 = []
        data = data.split()
        for word in data:
            if word not in stopWord:
                text3.append(word)
        return text3



    def stemming(self, word):                                                               #takes all the root words from stem_word and adds them to a list
        words = [self.stem_word(w) for w in word]
        l = list(words)
        return l
        
    

    def stem_word(self,word):                                                               #takes a word and checks wether its size is greater than the suffixes given below and if it is greater then checks weather such suffixes are present or not and cretaes a root word and sends it to stemming
        suffix = {
            1: ["ो","े","ू","ु","ी","ि","ा"],
            2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
            3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
            4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
            5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
        }

        for L in range(1,6):
            if len(word) > L + 1:
                for sf in suffix[L]:
                    if word.endswith(sf):
                        return (word[:-L])
            
        return word

if __name__ == "__main__":
    obj = InvertedIndex()
