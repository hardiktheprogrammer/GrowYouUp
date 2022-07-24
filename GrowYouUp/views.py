from django.shortcuts import render
from django.http import HttpResponse


def page_not_found_view(request, exception):
    return render(request, 'error404.html', status=404)

def handler403(request, *args, **argv):
    return HttpResponse('BLOCKED FOR 24HRS')