from django.http import HttpResponse

from django.shortcuts import render


def home(request):
  peoples =[
      {'name': 'John', 'age': 25},
      {'name': 'Jane', 'age': 30},
      {'name': 'Mark', 'age': 17},
      {'name': 'Anna', 'age': 18}
  ]
  vegetables = [
    'Carrot', 
    'Tomato', 
     'Cucumber', 
    'Onion', 
   'Broccoli', 
  ]

  return render (request, 'home/index.html', context={'page':'Django 2023 tutorial','peoples':peoples, 'vegetables':vegetables})
def about(request):
    context={'page': 'about'}
    return render (request, 'home/about.html', context)

def contact(request):
    context={'page': 'contact'}
    return render (request, 'home/contact.html', context)

def success_page(request):
 
    
    return HttpResponse("<H1> Hey this is a Success! Page</H1>")