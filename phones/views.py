from django.http import HttpRequest
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request: HttpRequest):
    return redirect('catalog')


def show_catalog(request: HttpRequest):

    list_phone = Phone.objects.all()

    if 'sort' in request.GET:
        parameter = request.GET.get('sort')
        
        if parameter == 'name':
            key = lambda x: x.name
            reverse = False

        elif parameter == 'min_price':
            key = lambda x: x.price
            reverse = False

        elif parameter == 'max_price':
            key = lambda x: x.price
            reverse = True

        list_phone = sorted(list_phone, key=key, reverse=reverse)

    template = 'catalog.html'
    context = {'phones': list_phone}
    return render(request, template, context)


def show_product(request: HttpRequest, slug: str):

    object = Phone.objects.filter(slug=slug)[0]

    template = 'product.html'
    context = {
        'phone': object
    }
    return render(request, template, context)
