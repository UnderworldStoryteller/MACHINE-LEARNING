读取words.txt中所有英文单字，显示第一次出现位置和出现次数
import sys
import string
#import collections
 
words = {} 

 
strip = string.whitespace + string.punctuation + string.digits + "\"'"
 

for line in open("words.txt"):
    for word in line.split():
        word = word.strip(strip)
        if len(word) >= 2:
            words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word,words[word]))
