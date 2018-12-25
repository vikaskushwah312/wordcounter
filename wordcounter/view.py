
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return  HttpResponse("<h1>Hello homepage </h1>")
    return render(request, 'home.html', {'name': 'hi there vikas singh kushwah'})
def about (request):
    return render(request, 'about.html')

def count(request):
    data = request.GET['fulltextarea']
    list = data.split()
    total_word = len(list)
    word_counter = {}

    for word in list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    short_word_counter = sorted(word_counter.items())

    return render(request, 'count.html', {'web': "word counter", 'total_word': total_word, 'word_counter':word_counter })

def contact(request):
    return  HttpResponse("<h1>contact</h2><br><span>This is our contact page ok</span>")