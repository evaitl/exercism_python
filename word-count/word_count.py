import re
from collections import Counter
rex = re.compile("(([a-z]+('[a-z]+)?)|[0-9])")
def count_words(sentence):
    return Counter(i[0] for i in rex.findall(sentence.lower()))
