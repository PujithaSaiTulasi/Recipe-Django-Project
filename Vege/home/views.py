from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hey! I am a Django Server")

def home_html(request):
   return HttpResponse("""<h1>Hey I am a Django Server</h1>
                       <p> Hey this is coming from Django server </p>
                       <hr>
                       <h3 style="color:red"> Hope you are loving it :) </h3>
                       """)
# def home(request):
#    return render(request, "index.html")

def home(request):
   people = [
       {'name' : 'Blessy Jayamon', 'age': 24},
       {'name' : 'Arya Rajan', 'age': 20},
       {'name' : 'Mounika Ruppa', 'age': 16},
       {'name' : 'Gayatri Ummidi', 'age': 30},
       {'name' : 'Keerthi Kunchi', 'age': 52},
       {'name' : 'Bhargavi Gummadi', 'age': 65},
   ]
   return render(request, "index.html", context = {'people': people})

def about(request):
   return render(request, "about.html")

def contact(request):
   return render(request, "contact.html")

def success_page(request):
   return HttpResponse("<h1> Hey this is a Success Page<h1>")