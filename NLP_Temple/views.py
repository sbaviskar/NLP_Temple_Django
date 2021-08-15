from django.http import HttpResponse
from django.shortcuts import render 
import nltk
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
    sent_tokens = nltk.sent_tokenize(raw_text)   # Sentence Segmenation A.K.A Sentence tokenization 
    return render(request,'sentSegmentation.html',{'tokens':sent_tokens}) 

def wordTokenization(request): 
    return render(request,'wordTokenization.html') 

def posTag(request):
    return render(request,'posTaging.html')
