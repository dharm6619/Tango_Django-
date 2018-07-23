from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    context = RequestContext(request)
    context_dict = {'name':'Dharmendra'}
    return render_to_response('rango/index.html',context_dict,context)

def about(request):
    return HttpResponse("Rango says hello world from my side!  <a href='/rango/'> Return</a>")
