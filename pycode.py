FirstFile = open(r"Beyond the Wall of Sleep.txt","r",encoding="utf-8")
ReadFirstFile = FirstFile.read()  #Read the first book
RFFL = ReadFirstFile.lower()  #Make all letters lowercase
Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
WordsInFF = ""  #To get the first file without punctuations
for char in RFFL:
   if char not in Punctuations:
       WordsInFF = WordsInFF + char

WordsInFFS = WordsInFF.split()  #Splits a string into a list

SecondFile = open(r"Pride and Prejudice.txt","r",encoding="utf-8")
ReadSecondFile = SecondFile.read()  #Read the second book
RSFL = ReadSecondFile.lower()  #Make all letters lowercase
WordsInSF = ""  #To get the second file without punctuations
for char in RSFL:
   if char not in Punctuations:
       WordsInSF = WordsInSF + char

WordsInSFS = WordsInSF.split()  #Splits a string into a list

#Get the common words between two books
common = set(WordsInFFS).intersection(set(WordsInSFS))

print(common)