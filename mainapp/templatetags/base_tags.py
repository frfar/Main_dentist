from django import template
from . .models import Category

register = template.Library()

@register.inclusion_tag("mainapp/partials/carousel_loop.html")
def carousel_loop():
    return{
        "category": Category.objects.get(title='carousel')
    }


@register.inclusion_tag("mainapp/partials/service_loop.html")
def service_loop():
    return{
        "category": Category.objects.get(title='service')
    }


@register.inclusion_tag("mainapp/partials/natices_loop.html")
def natices_loop():
    return{
        "category": Category.objects.get(title='notices')
    }

@register.inclusion_tag("mainapp/partials/important_loop.html")
def important_loop():
    return{
        "category": Category.objects.get(title='important')
    }

@register.inclusion_tag("mainapp/partials/new_uptodate.html")
def new_uptodate():
    return{
        "category": Category.objects.get(title='new_uptodate')
    }

@register.inclusion_tag("mainapp/partials/about_loop.html")
def about_loop():
    return{
        "category": Category.objects.get(title='about')
    }