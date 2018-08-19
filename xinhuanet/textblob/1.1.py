from textblob import TextBlob

txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
actions between computers and human (natural) languages."""

blob = TextBlob(txt)
print(blob.noun_phrases)
# [u'natural language processing', 'nlp', u'computer science', u'artificial intelligence', u'computational linguistics']
