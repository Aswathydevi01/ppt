def lines(a,b):
    alist = set(a.split("\n"))
    blist = set(b.split("\n"))
    return list(alist & blist)
from nltk.tokenize import sent_tokenize
def sentences(a,b):
    alist = set(sent_tokenize(a))
    blist = set(sent_tokenize(b))
    return list(alist & blist)
