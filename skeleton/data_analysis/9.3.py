import nltk
from sklearn.feature_extraction.text import CountVectorizer

#9.3词袋模型
gb = nltk.corpus.gutenberg
print gb.fileids()

hamlet = gb.raw("shakespeare-hamlet.txt")
macbeth = gb.raw("shakespeare-macbeth.txt")

print len(hamlet)
print len(macbeth)

cv = CountVectorizer(stop_words='english')
print "Feature vector", cv.fit_transform([hamlet, macbeth]).toarray()[0]
print "Feature vector", cv.fit_transform([hamlet, macbeth]).toarray()[1]
print "Features", len(cv.get_feature_names())
print "Features", cv.get_feature_names()[0:3]
print "Features", cv.get_feature_names()[6207:6210]
