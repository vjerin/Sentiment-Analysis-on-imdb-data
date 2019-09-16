from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from nltk import word_tokenize
wordnet_tags=['n','v']
lem=WordNetLemmatizer()

def word_features(doc):
    tagged=pos_tag(word_tokenize(doc))
    
    doc_=[]
    for token,tag in tagged:
        if tag=='NNPS' or tag=='NNP' or tag=='POS' or tag==token: 
            pass
        elif tag[0].lower() in wordnet_tags:
            doc_.append(lem.lemmatize(token.lower(),tag[0].lower()))
        else :
            doc_.append(token.lower())
    doc_x=' '.join(doc_).strip() 
    return doc_x