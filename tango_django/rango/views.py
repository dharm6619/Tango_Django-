from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.http import HttpResponse

from .models import Category, page

from .forms import CategoryForm, pageForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

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


@csrf_exempt
def category(request,category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_',' ')
    context_dict =  {'category_name':category_name,
    'category_name_url':category_name_url}
    try:
        category = Category.objects.get(name = category_name)
        Pages = page.objects.filter(category=category)
        context_dict['pages'] = Pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    
    return render_to_response('rango/category.html',context_dict,context)


@csrf_exempt
def add_category(request):
    print(request)
    print("inside the add_category method")
    print(request.method)
    context = RequestContext(request)
    if request.method == 'POST':
        print("inside post script method")
        print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render_to_response('rango/add_category.html', {'form': form}, context)

@csrf_exempt
def add_page(request, category_name_url):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict['cat_list'] = cat_list

    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            except Category.DoesNotExist:
                return render_to_response( 'rango/add_page.html',context_dict,context)
            page.views = 0
            page.save()
            return category(request, category_name_url)
        else:
            print (form.errors())
    else:
        form = PageForm()
    context_dict['category_name_url']= category_name_url
    context_dict['category_name'] =  category_name
    context_dict['form'] = form

    return render_to_response( 'rango/add_page.html',context_dict,context)

# def add_page(request,category_name_url):
#     context = RequestContext(request)
#     category_name = decode_url(category_name_url)
#     if request.method == 'POST':
#         form = PageForm(request.POST)
#         if form.is_valid():
#             page = form.save(commit=False)
#             try:
#                 cat = Category.objects.get(name=category_name)
#                 page.category = cat
#             except Category.DoesNotExist:
#                 return render_to_response('rango/add_page.html',context_dict,context)
#             page.views = 0
#             page.save()
#             return category(request, category_name_url)
#         else:
#             print (form.errors)
#     else:
#         form = pageForm()
#     return render_to_response('rango/add_page.html',context_dict,context)
