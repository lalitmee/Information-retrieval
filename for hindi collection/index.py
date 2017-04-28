import os
import pickle
import xml.etree.ElementTree as ET

# Giving Path of the files on the Desktop
path = "/home/lalit/Desktop/IR_LAB/Final_Index/hindi/"

# declaring an array for all files to store

# declaring a dictionary for counting the words
freq = {}
# declaring a dictionary for storing the indexes
inverted = {}

# a text file for writing the counts of the words in all the files
# fo = open('wordcount.txt', 'w')

fo = open('words.txt', 'w+')

# list oft he words which have to be removed for stemming
suffixes = {
    1: [u"ो", u"े", u"ू", u"ु", u"ी", u"ि", u"ा"],
    2: [u"कर", u"ाओ", u"िए", u"ाई", u"ाए", u"ने", u"नी", u"ना", u"ते", u"ीं", u"ती", u"ता", u"ाँ", u"ां", u"ों",
        u"ें"],
    3: [u"ाकर", u"ाइए", u"ाईं", u"ाया", u"ेगी", u"ेगा", u"ोगी", u"ोगे", u"ाने", u"ाना", u"ाते", u"ाती", u"ाता",
        u"तीं", u"ाओं", u"ाएं", u"ुओं", u"ुएं", u"ुआं"],
    4: [u"ाएगी", u"ाएगा", u"ाओगी", u"ाओगे", u"एंगी", u"ेंगी", u"एंगे", u"ेंगे", u"ूंगी", u"ूंगा", u"ातीं", u"नाओं",
        u"नाएं", u"ताओं", u"ताएं", u"ियाँ", u"ियों", u"ियां"],
    5: [u"ाएंगी", u"ाएंगे", u"ाऊंगी", u"ाऊंगा", u"ाइयाँ", u"ाइयों", u"ाइयां"],
}
c = 0
# getting filename in the array files
for filename in os.listdir(path):
    # print(filename)
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

    data = root[0].text + root[2].text

    # removing punctuations from the data
    data = data.replace('\n', ' ')
    data = data.replace('(', '')
    data = data.replace(')', '')
    data = data.replace('?', '')
    data = data.replace(',', '')
    data = data.replace('।', '')
    data = data.replace('॥', '')
    data = data.replace(':', '')
    data = data.replace('!', '')
    data = data.replace('-', ' ')
    data = data.replace('.', '')
    data = data.replace("'", '')
    data = data.replace("  ", ' ')
    data = data.replace("/", ' ')
    data = data.replace("@", '')
    data = data.replace("%", '')
    data = data.replace("...", '')
    data = data.replace("=", ' ')
    data = data.split()
    #fo.write(str(data))
    
    #fo.write("%s \t\t\t %s " % (i, str(freq[i]) + '\n'))


    # Reading the file of stopwords to remove all the stopwords from all the files
    fi = open('stopwords.txt', 'r')
    stop = fi.read().split('\n')
    # fo.write(str(stop))
    stemwords = []
    # scanning all the parsed data
    for word in data:
        if word not in stop:  # removing the stopwords from the parsed data

            for l in 5, 4, 3, 2, 1:
                if len(word) > l + 1:
                    for suf in suffixes[l]:  # taking the suffixes in suf variable
                        if word.endswith(suf):  # checking the for the suffixes in the parsed words
                            stemwords.append(word[:-l])

                            # creating the dictionary of words after steming

    single = list(stemwords)  # creating the list of the words after removing repeatition



    if True:
        for i in set(single):
            if i in inverted.keys():  # checking for the word if it is in the inverted keys list
                inverted[i].append((filename, single.count(i)))  # if it also in another file, updating the
                # list of filenames
            else:
                inverted[i] = [(filename, single.count(i))]  # otherwise it will remain same

f = open('inverted.txt', 'w')  # writing a file named 'inverted.txt' to store the list of inverted index
# print(inverted)
for i in inverted.keys():
    f.write(str(i) + '\t\t')  # writing the word in the file
    f.write(str(inverted.get(i)) + '\n')  # writing the filenames
# word = input()
# for i in inverted:
#	print('{0} - {1}'.format(i, inverted[i]), end="\n\n\n")

# print(inverted.get(word))
f.close()

pickle.dump(inverted, open("Inverted_Index.p", "wb"))  # dumping the data in a file and writing a binary file




