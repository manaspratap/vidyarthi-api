import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


def string_check(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            word = word_tokenize(line)
            if string_to_search in word:
                return True
    return False

def token(sentence):
    word_tokens=word_tokenize(sentence)
    word_tokens_cleaned={word for word in word_tokens if word not in stop_words}
    return ' '.join(list(word_tokens_cleaned))

def getPage(searchWord):
    navigateToPage="support"
    learn=0
    work=0
    text = searchWord
    mytext=text.lower()
    stop_words = set(stopwords.words('english'))
    cleaned_text=token(mytext)
    mytext=text.lower()
    Tokenized=word_tokenize(cleaned_text)
    words = [word for word in Tokenized if word.isalpha()]
    w1 = wordnet.synset('learn.v.01')
    w2 = wordnet.synset('work.v.01')
    for i in words:
        navigateToPage_word = wordnet.synsets(i)
        for j in navigateToPage_word:
            xd=w1.wup_similarity(j)
            if learn<xd:
                learn=xd
            cd=w2.wup_similarity(j)
            if work<cd:
                work=cd
    if learn>work:
        navigateToPage = "course"
    elif work>learn:
        navigateToPage = "collaborate"
    elif work==learn:
        for i in words:
            if string_check("file_learn.txt", i):
                navigateToPage = "course"
                break
            elif string_check("file_work.txt", i):
                navigateToPage = "collaborate"
                break
            else:
                navigateToPage = "support"
    return navigateToPage