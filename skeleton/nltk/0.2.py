import nltk
from nltk.corpus import treebank

sentence = """At eight o'clock on Thursday morning
              Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

print tokens

tagged = nltk.pos_tag(tokens)

print "Nums :%d , Tokens: %s" % (len(tagged), tagged)

entities = nltk.chunk.ne_chunk(tagged)

print entities

entities.draw()

#t = treebank.parsed_sents('wsj_0001.mrg')[0]
#t.draw()