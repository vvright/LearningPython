from nltk.book import *

print text1.concordance("monstrous")

print text2.common_contexts(["monstrous", "very"])

print text1.similar("monstrous")

print text2.similar("monstrous")

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])