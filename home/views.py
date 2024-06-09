from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import About, Contact

from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from django.contrib import messages


def home(request):
    aboutme = About.objects.values().all()
    template = loader.get_template('home.html')
    context = {
        'aboutme' : aboutme
    }
    return HttpResponse(template.render(context, request))

def index(request):
    aboutme = About.objects.values().all()
    template = loader.get_template('home.html')
    context = {
        'aboutme' : aboutme
    }
    return HttpResponse(template.render(context, request))

   
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
#for contact form
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')  # Replace 'success' with your actual success URL name
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def messages(request):
    mycontacts = Contact.objects.all().values()
    context = {
        'mycontacts' : mycontacts
    }


    template = loader.get_template('messages.html')
    return HttpResponse(template.render(context, request))





