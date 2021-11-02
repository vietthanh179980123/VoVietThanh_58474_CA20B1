"""
Author: Vo Viet Thanh
Date: 10/10/2021
Program:A file concordance tracks the unique words in a file and their frequencies. Write
a program that displays a concordance for a file. The program should output the
unique words and their frequencies in alphabetical order. Variations are to track
sequences of two words and their frequencies, or n words and their frequencies.
Solution:
    ....
"""
import re
fre={}
document_text = open('test.txt','r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b [a-z]{1-15} \b',text_string)
for word in match_pattern:
    count = fre.get(word,0)
    fre[word]=count+1
fre_list = fre.keys()
for words in sorted(fre_list):
    print(words,fre[words])
