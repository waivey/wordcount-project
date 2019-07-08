from django.http import HttpResponse
from django.shortcuts import render
import operator
import re


def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']

	fulltext_nopunc = re.sub(r'[^\w\s]', '',fulltext)

	wordlist = fulltext_nopunc.lower().split()

	worddict = {}

	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1

	sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
	
	print(fulltext)
	return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
	return render(request, 'about.html')