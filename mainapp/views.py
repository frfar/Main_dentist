from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Article, Category

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    context = {
        'articles': Article.objects.filter(status="p").all()
    }
    return render(request, 'mainapp/index.html', context)

def category(request, slug):
    context = {
        "category" : get_object_or_404(Category, slug=slug, status="True")
    }
    return render(request, "mainapp/category.html", context)

def about(request):
    context = {
        'articles': Article.objects.filter(status="p").all()
    }
    return render(request, "mainapp/about.html", context)

def service(request):
    service = Category.objects.get(title='service')
    context = {
        'articles': service.articles.filter(status="p").all()
    }
    return render(request, "mainapp/service.html", context)

def service_detail(request, slug):
    service = Category.objects.get(title='service')
    context = {
        'article': service.articles.get(slug=slug)
    }
    return render(request, "mainapp/service-detail.html", context)

def patients(request):
    patient = Category.objects.get(title='patient')
    context = {
        'articles': patient.articles.filter(status="p").all()
    }
    return render(request, "mainapp/patients.html", context)

def testimonials(request):
    testimonial = Category.objects.get(title='testimonial')
    context = {
        'articles': testimonial.articles.filter(status="p").all()
    }
    return render(request, 'mainapp/testimonials.html', context)

def contact(request):
    context = {}
    return render(request, "Mainapp/contact.html", context)

def sendEmail(request):

    if request.method == 'POST':
        template = render_to_string('Mainapp/email_template.html' , {
            'name':request.POST['name'],
            'phone':request.POST['phone'],
            'email':request.POST['email'],
            'message':request.POST['message'],
            })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['babakamiri.rahimi@gmail.com']
            )
        email.fail_silently= False
        email.send()
    return render(request, "Mainapp/email_sent.html")
