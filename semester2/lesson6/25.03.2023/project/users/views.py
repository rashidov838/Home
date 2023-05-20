from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    # return HttpResponse("Hello World")
    template=loader.get_template('helloworld.html')
    return HttpResponse(template.render())