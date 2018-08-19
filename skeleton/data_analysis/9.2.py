# coding=utf-8
import nltk

'''

sw = set(nltk.corpus.stopwords.words('english'))
#print len(list(sw))
print "Stop words", list(sw)[:]
#print sw

#print "i" in sw

gb = nltk.corpus.gutenberg
print len(gb.fileids())
print "Gutenberg files", gb.fileids()[-5:]

#print len(gb.sents("milton-paradise.txt"))

text_sent = gb.sents("milton-paradise.txt")[:2]
print "Unfiltered", text_sent

for sent in text_sent:
    filtered = [w.lower() for w in sent if w.lower() not in sw]
    print "Filtered", filtered
    tagged = nltk.pos_tag(filtered)
    print "Tagged", tagged

#test_str = u"我爱北京"
#print test_str

'''
print nltk.pos_tag(['who', 'whose', 'which', 'where', 'how', 'when', 'this', 'some'])
