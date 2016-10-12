from django.shortcuts import render

def index_view(request):
    text = "TESTING"
    context = {'text1': text, 'text2': "text2 testing"}
    return render(request, 'users/index/index.html', context)

def writer(request):
    text = "TESTING"
    context = {'text1': text, 'text2': "text2 testing"}
    return render(request, 'users/index/index.html', context)

def client(request):
    text = "TESTING"
    context = {'text1': text, 'text2': "text2 testing"}
    return render(request, 'users/index/index.html', context)
