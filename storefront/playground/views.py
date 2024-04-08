from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response

def say_hello(request):
    #Pull data from db
    #Transform
    #Send email
    return render(request, 'hello.html', {'name':'Steve'})