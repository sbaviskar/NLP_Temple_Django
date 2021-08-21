from django.http import HttpResponse
from django.shortcuts import render 
import nltk
from nltk.corpus.reader.wordnet import NOUN
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize #
from nltk.corpus import stopwords,brown
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer  # used for lemming



def home(request):
    text = "Data data " 
    sent_token = sent_tokenize(text)
    word_token = nltk.word_tokenize(text)
    return render(request,'home.html',{'word_token':word_token}) 


def sentSegment(request): 
    raw_text = request.GET['allRawText']             # fetch raw text from user 
    sent_token_list = nltk.sent_tokenize(raw_text)   # Sentence Segmenation A.K.A Sentence tokenization 
    return render(request,'sentSegmentation.html',{'tokens':sent_token_list}) 

def wordTokenization(request):                      ## function for word_Tokenixation
    raw_text = request.GET['allRawText']            # fetch raw text from user
    word_token_list = nltk.word_tokenize(raw_text)  # Word Tokenization
    print(type(word_token_list))
    print(type(word_token_list))
    return render(request,'wordTokenization.html',{'tokens':word_token_list}) 

def posTag(request):
    raw_text = request.GET['allRawText']   # fetch raw text from user
    word_token_list= word_tokenize(raw_text)   # Word Tokenization
    pos_tag_list = nltk.pos_tag(word_token_list,lang="eng",tagset=brown) # pos_taging
    return render(request,'posTaging.html',{'POS_tags':pos_tag_list})

def lemmatization(request):
    raw_text = request.GET['allRawText']  

   # Normalize text
   # NLTK considers capital letters and small letters differently.
   # For example, Fox and fox are considered as two different words.
   # Hence, we convert all letters of our text into lowercase.
    lower_case_raw_text = raw_text.lower()           # Converting text into lowercase
    words = nltk.word_tokenize(lower_case_raw_text)  # tokenize text

    lemmatizer = WordNetLemmatizer()  # Loading lemmatizer Module
    words_lemma = []
    for word in words:
	    words_lemma.append(lemmatizer.lemmatize(word ,pos = NOUN))
    
    print(words_lemma)
    return render(request,'lemmatization.html',{'lemma' : words_lemma,'origin':words})



def stemming(request):
    raw_text = request.GET['allRawText']        # fetch raw text from user
    lower_case_raw_text = raw_text.lower()      # Converting text into lowercase
    word_token_list = nltk.word_tokenize(lower_case_raw_text)       # Word Tokenization
    
    
    snow_stem = SnowballStemmer(language='english')  # Loading Stemmer Module
    stem_words_list = [] 
   
    for w in word_token_list:
     stem_words_list.append(w+'  >--------->  '+snow_stem.stem(w))

    return render(request,'stemming.html',{'stems':stem_words_list})
