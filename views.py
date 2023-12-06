from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'Name':'Pratik','Place':'Earth'}
    return render(request,'index.html',params)

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Punctuations', 'analyed_text' : analyzed} 
        djtext = analyzed
                
        if(fullcaps== 'on'):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose' : 'Changed to Uppercase', 'analyed_text' : analyzed} 
            djtext = analyzed

            if(newlineremover == 'on'):
                analyzed = ""
                for char in djtext:
                    if char != '\n' and char != '\r':
                        analyzed = analyzed + char
                params = {'purpose' : 'New Line Removed', 'analyed_text' : analyzed} 
                djtext = analyzed
    
                if(spaceremover == 'on'):
                    analyzed = ""
                    for index,char in enumerate(djtext):
                        if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                            analyzed = analyzed + char
                    params = {'purpose' : 'Space Removed', 'analyed_text' : analyzed} 
                    djtext = analyzed

    elif(charcount == 'on'):
        count = 0
        analyzed = ""
        for char in djtext:
            if (char != ' ' and char != '\n' and char != '\r'):
                count += 1
                analyzed = count
        params = {'purpose' : 'Character Count', 'analyed_text' : analyzed}  
        return render(request,'analyze.html',params)


    else:
        return HttpResponse('Error')

    return render(request,'analyze.html',params)

