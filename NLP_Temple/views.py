from django.http import HttpResponse
from django.shortcuts import render 
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize #
from nltk.corpus import stopwords 
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer


 


def home(request):
    text = "Data data " 
    sent_token = sent_tokenize(text)
    word_token = nltk.word_tokenize(text)
    return render(request,'home.html',{'word_token':word_token}) 


def sentSegment(request): 
    raw_text = request.GET['allRawText']        # fetch raw text from user 
    sent_token_list = nltk.sent_tokenize(raw_text)   # Sentence Segmenation A.K.A Sentence tokenization 
    return render(request,'sentSegmentation.html',{'tokens':sent_token_list}) 

def wordTokenization(request):              ## function for word_Tokenixation
    raw_text = request.GET['allRawText']        # fetch raw text from user
    word_token_list = nltk.word_tokenize(raw_text)       # Word Tokenization
    print(type(word_token_list))
    print(type(word_token_list))
    return render(request,'wordTokenization.html',{'tokens':word_token_list}) 

def posTag(request):
    raw_text = request.GET['allRawText']   # fetch raw text from user
    word_token_list= word_tokenize(raw_text)   # Word Tokenization
    pos_tag_list = nltk.pos_tag(word_token_list,lang="eng") # pos_taging
    return render(request,'posTaging.html',{'sen':pos_tag_list})
