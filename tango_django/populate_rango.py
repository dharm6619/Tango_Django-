import os
def populate():
    python_cat = add_cat('Python')
    
    add_page(cat = python_cat,
    title = "Official Python Tutorial",
    url = "http://docs.python.org/")

    add_page(cat = python_cat,
    title = "For Data Science",
    url = "http://www.dataquest.io/")

    add_page(cat = python_cat,
    title = "For Basic Practice Problems",
    url = "http://www.hackerrank.com/")

    django_cat = add_cat("Django")

    add_page(cat = django_cat,
    title = "Official Django Tutorial",
    url = "https://docs.djangoproject.com/en/2.0/")

    add_page(cat = django_cat,
    title = "Other Source",
    url = "https://djangoforbeginners.com/")

    frame_cat = add_cat("Other Frameworks")
    add_page(cat=frame_cat,
    title="Bottle",
    url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
    title="Flask",
    url="http://flask.pocoo.org")
    # Print out what we have added to the user.
    #for c in Category.objects.all():
     #   for p in Page.objects.filter(category=c):
      #      print "- {0} - {1}".format(str(c), str(p))
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

if __name__ == '__main__':
    print ("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.˓ → settings')
    from rango.models import Category, Page
    populate()

    