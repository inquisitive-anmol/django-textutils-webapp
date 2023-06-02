# I have created this
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    # print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    # print(removepunc)
    if removepunc == 'on':
        purpose = "Removed Punctuations"
        puntuations = ''''`~!@#$%^&*(){}[];'"\|<>?/,:."-=_+'''
        analyzed = ''
        for char in djtext:
            if char not in puntuations:
                analyzed += char
    if (capitalize == 'on'):
        if removepunc == 'on':
            purpose = "Removed Punctuations and Capitalized"
            puntuations = ''''`~!@#$%^&*(){}[];'"\|<>?/,:."-=_+'''
            analyzed = ''
            for char in djtext:
                if char not in puntuations:
                    analyzed += char.upper()
        else:
            purpose = "Capitalized"
            analyzed = djtext.upper()


    elif removepunc == 'off' and capitalize == 'off':
        return HttpResponse("Choose atleast one action from the checkboxes ")

    params = {'analyzed_text': djtext, 'purpose': purpose, 'purpose_comptd':analyzed}
    return render(request, 'analyze.html',params)
    # return HttpResponse("removepunc")

def about(request):
    return  HttpResponse('''<h1 style="background-color:DodgerBlue; color:red">Welcome to the about page of my first django web app</h1>''')
