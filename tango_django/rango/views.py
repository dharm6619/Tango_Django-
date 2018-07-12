from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.http import HttpResponse

from .models import Category, page

from .forms import CategoryForm

# Create your views here.

def index(request):
    context = RequestContext(request)
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    for category in category_list:
        category.url = category.name.replace('_', ' ')
    return render_to_response('rango/index.html',context_dict,context)

def about(request):
    context = RequestContext(request)
    dict1 = {'name':'Dharmendra Mishra',
    'age':21,
    'DOB':'07/05/1998'}
    return render_to_response('rango/about.html',dict1,context)



def category(request,category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_',' ')
    context_dict =  {'category_name':category_name}
    try:
        category = Category.objects.get(name = category_name)
        Pages = page.objects.filter(category=category)
        context_dict['pages'] = Pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    
    return render_to_response('rango/category.html',context_dict,context)

def add_category(request):
    # Get the context from the request.
    # context = RequestContext(request)
    # # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
        return render_to_response('rango/add_category.html', {'form': form}, context)


